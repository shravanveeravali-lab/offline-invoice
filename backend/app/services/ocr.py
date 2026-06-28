from pathlib import Path

import pytesseract
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFInfoNotInstalledError
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

SUPPORTED_IMAGES = {".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".webp"}


class OCRService:
    def extract_text(self, file_path: Path) -> str:
        suffix = file_path.suffix.lower()

        if suffix == ".txt":
            return file_path.read_text(encoding="utf-8")

        if suffix == ".pdf":
            return self._extract_pdf(file_path)

        if suffix in SUPPORTED_IMAGES:
            return self._extract_image(file_path)

        raise ValueError(f"Unsupported file type: {suffix}")

    def _extract_pdf(self, file_path: Path) -> str:
        try:
            pages = convert_from_path(str(file_path), dpi=220)
            return "\n\n".join(
                pytesseract.image_to_string(page)
                for page in pages
            )
        except PDFInfoNotInstalledError:
            raise ValueError(
                "PDF processing requires Poppler. Please upload an image invoice (.png/.jpg) or install Poppler."
            )

    def _extract_image(self, file_path: Path) -> str:
        with Image.open(file_path) as image:
            return pytesseract.image_to_string(image)