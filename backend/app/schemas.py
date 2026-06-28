from pydantic import BaseModel, Field


class InvoiceItemBase(BaseModel):
    description: str
    quantity: float = Field(ge=0)
    price: float = Field(ge=0)
    subtotal: float = Field(ge=0)


class InvoiceExtraction(BaseModel):
    vendor_name: str
    invoice_number: str
    invoice_date: str
    currency: str = "INR"
    gst: float = Field(ge=0, default=0)
    items: list[InvoiceItemBase] = Field(default_factory=list)
    subtotal: float = Field(ge=0, default=0)
    total: float = Field(ge=0, default=0)
    confidence_score: float = Field(ge=0, le=1, default=0.5)


class UploadResponse(BaseModel):
    filename: str
    stored_path: str


class ExtractRequest(BaseModel):
    stored_path: str


class InvoiceResponse(InvoiceExtraction):
    id: int
    source_filename: str
    created_at: str


class HistoryResponse(BaseModel):
    invoices: list[InvoiceResponse]
