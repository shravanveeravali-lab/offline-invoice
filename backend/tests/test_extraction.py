from app.config import Settings
from app.services.cleaning import clean_ocr_text
from app.services.llm import LocalLLMService


def test_clean_ocr_text_compacts_spacing() -> None:
    assert clean_ocr_text("A   B\n\n\nC") == "A B\n\nC"


def test_deterministic_invoice_extraction() -> None:
    service = LocalLLMService(Settings())
    result = service.extract_invoice(
        """
        ABC Electronics
        Invoice No: INV-1024
        Date: 2026-06-27
        Keyboard 2 1200 2400
        GST: 432
        Total: 2832
        """
    )
    assert result.vendor_name == "ABC Electronics"
    assert result.invoice_number == "INV-1024"
    assert result.currency == "INR"
    assert result.total == 2832
    assert result.items[0].description == "Keyboard"
