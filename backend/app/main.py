from pathlib import Path
from typing import Annotated
from uuid import uuid4

from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session, selectinload

from app.config import get_settings
from app.database import get_db, init_db
from app.models import Invoice
from app.schemas import ExtractRequest, HistoryResponse, InvoiceResponse, UploadResponse
from app.services.cleaning import clean_ocr_text
from app.services.llm import LocalLLMService
from app.services.ocr import OCRService
from app.services.storage import list_invoices, save_invoice, to_response

settings = get_settings()
app = FastAPI(title=settings.app_name, version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
ocr_service = OCRService()
llm_service = LocalLLMService(settings)


@app.on_event("startup")
def on_startup() -> None:
    settings.upload_dir.mkdir(parents=True, exist_ok=True)
    init_db()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "mode": "offline"}


@app.post("/upload", response_model=UploadResponse)
async def upload(file: Annotated[UploadFile, File()]) -> UploadResponse:
    suffix = Path(file.filename or "").suffix.lower()
    if suffix not in {".pdf", ".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".webp", ".txt"}:
        raise HTTPException(status_code=400, detail="Unsupported file type")
    stored_name = f"{uuid4().hex}{suffix}"
    settings.upload_dir.mkdir(parents=True, exist_ok=True)
    stored_path = settings.upload_dir / stored_name
    stored_path.write_bytes(await file.read())
    return UploadResponse(filename=file.filename or stored_name, stored_path=str(stored_path))


@app.post("/extract", response_model=InvoiceResponse)
def extract(payload: ExtractRequest, db: Annotated[Session, Depends(get_db)]) -> InvoiceResponse:
    file_path = Path(payload.stored_path)
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Uploaded file not found")
    try:
        raw_text = ocr_service.extract_text(file_path)
        print("\n===== OCR TEXT =====")
        print(raw_text)
        print("====================")
        cleaned_text = clean_ocr_text(raw_text)
        extraction = llm_service.extract_invoice(cleaned_text)
        invoice = save_invoice(db, extraction, file_path.name, cleaned_text)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return to_response(invoice)


@app.get("/invoice/{invoice_id}", response_model=InvoiceResponse)
def get_invoice(invoice_id: int, db: Annotated[Session, Depends(get_db)]) -> InvoiceResponse:
    invoice = (
        db.query(Invoice)
        .options(selectinload(Invoice.items))
        .filter(Invoice.id == invoice_id)
        .first()
    )
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return to_response(invoice)


@app.get("/history", response_model=HistoryResponse)
def history(db: Annotated[Session, Depends(get_db)], q: str | None = None) -> HistoryResponse:
    return HistoryResponse(invoices=[to_response(invoice) for invoice in list_invoices(db, q)])


@app.delete("/invoice/{invoice_id}")
def delete_invoice(invoice_id: int, db: Annotated[Session, Depends(get_db)]) -> dict[str, str]:
    invoice = db.get(Invoice, invoice_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    db.delete(invoice)
    db.commit()
    return {"status": "deleted"}
