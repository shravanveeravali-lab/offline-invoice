from sqlalchemy import or_, select
from sqlalchemy.orm import Session, selectinload

from app.models import Invoice, InvoiceItem, ProcessingLog
from app.schemas import InvoiceExtraction, InvoiceResponse


def save_invoice(
    db: Session,
    extraction: InvoiceExtraction,
    source_filename: str,
    raw_text: str,
) -> Invoice:
    invoice = Invoice(
        vendor_name=extraction.vendor_name,
        invoice_number=extraction.invoice_number,
        invoice_date=extraction.invoice_date,
        currency=extraction.currency,
        gst=extraction.gst,
        subtotal=extraction.subtotal,
        total=extraction.total,
        confidence_score=extraction.confidence_score,
        source_filename=source_filename,
        raw_text=raw_text,
    )
    invoice.items = [InvoiceItem(**item.model_dump()) for item in extraction.items]
    invoice.logs = [
        ProcessingLog(stage="extract", status="success", message="Invoice extracted offline")
    ]
    db.add(invoice)
    db.commit()
    db.refresh(invoice)
    return invoice


def to_response(invoice: Invoice) -> InvoiceResponse:
    return InvoiceResponse(
        id=invoice.id,
        vendor_name=invoice.vendor_name,
        invoice_number=invoice.invoice_number,
        invoice_date=invoice.invoice_date,
        currency=invoice.currency,
        gst=invoice.gst,
        items=[
            {
                "description": item.description,
                "quantity": item.quantity,
                "price": item.price,
                "subtotal": item.subtotal,
            }
            for item in invoice.items
        ],
        subtotal=invoice.subtotal,
        total=invoice.total,
        confidence_score=invoice.confidence_score,
        source_filename=invoice.source_filename,
        created_at=invoice.created_at.isoformat(),
    )


def list_invoices(db: Session, query: str | None = None) -> list[Invoice]:
    statement = (
        select(Invoice).options(selectinload(Invoice.items)).order_by(Invoice.created_at.desc())
    )
    if query:
        like_query = f"%{query}%"
        statement = statement.where(
            or_(
                Invoice.vendor_name.ilike(like_query),
                Invoice.invoice_number.ilike(like_query),
                Invoice.currency.ilike(like_query),
                Invoice.invoice_date.ilike(like_query),
            )
        )
    return list(db.scalars(statement))
