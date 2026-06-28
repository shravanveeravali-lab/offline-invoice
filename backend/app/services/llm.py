import json
import re
import subprocess
from pathlib import Path

from app.config import Settings
from app.schemas import InvoiceExtraction, InvoiceItemBase


class LocalLLMService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def extract_invoice(self, text: str) -> InvoiceExtraction:
        if self._llama_ready():
            result = self._run_llama(text)
            if result:
                return result

        return self._deterministic_extract(text)

    def _llama_ready(self) -> bool:
        return (
            bool(self.settings.llama_cpp_bin)
            and bool(self.settings.tinyllama_gguf_path)
            and Path(self.settings.llama_cpp_bin).exists()
            and Path(self.settings.tinyllama_gguf_path).exists()
        )

    def _run_llama(self, text: str):
        prompt = f"""
Extract invoice information.

Return ONLY valid JSON.

Schema:

{{
"vendor_name":"",
"invoice_number":"",
"invoice_date":"",
"currency":"INR",
"gst":0,
"subtotal":0,
"total":0,
"confidence_score":0.95,
"items":[
{{
"description":"",
"quantity":1,
"price":0,
"subtotal":0
}}
]
}}

Invoice Text:

{text[:3500]}
"""

        command = [
            str(self.settings.llama_cpp_bin),
            "-m",
            str(self.settings.tinyllama_gguf_path),
            "-p",
            prompt,
            "-n",
            "512",
            "--temp",
            "0.1",
        ]

        try:
            completed = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=self.settings.llama_timeout_seconds,
            )
        except Exception:
            return None

        if completed.returncode != 0:
            return None

        match = re.search(r"\{.*\}", completed.stdout, re.DOTALL)

        if not match:
            return None

        try:
            return InvoiceExtraction.model_validate(
                json.loads(match.group(0))
            )
        except Exception:
            return None

    def _deterministic_extract(self, text: str) -> InvoiceExtraction:

        print("\n================ OCR TEXT ================\n")
        print(text)
        print("\n==========================================\n")

        lines = [l.strip() for l in text.splitlines() if l.strip()]

        vendor = "Unknown Vendor"

        vendor_keywords = [
            "amazon",
            "seller",
            "private",
            "ltd",
            "limited",
            "services",
            "solutions",
            "mart",
            "electronics",
            "retail",
            "store",
            "traders",
            "enterprise",
        ]

        for line in lines[:20]:
            lower = line.lower()

            if any(word in lower for word in vendor_keywords):
                vendor = line
                break

        invoice_number = self._first_match(
            text,
            [
                r"invoice\s*(?:no|number|#)\s*[:#-]?\s*([A-Z0-9\-]+)",
                r"inv\s*[:#-]?\s*([A-Z0-9\-]+)",
                r"(MKT[-0-9]+)",
            ],
            "UNKNOWN",
        )

        invoice_date = self._first_match(
            text,
            [
                r"([0-9]{2}/[0-9]{2}/[0-9]{4})",
                r"([0-9]{2}-[0-9]{2}-[0-9]{4})",
                r"([0-9]{4}-[0-9]{2}-[0-9]{2})",
            ],
            "Unknown",
        )

        currency = "INR"

        gst = 0

        gst_matches = re.findall(
            r"(?:gst|tax)\s*[:#-]?\s*(?:₹|Rs\.?|INR)?\s*([0-9,]+(?:\.[0-9]{1,2})?)",
            text,
            re.IGNORECASE,
        )

        if gst_matches:
            gst = max(float(x.replace(",", "")) for x in gst_matches)

        total = 0

        total_matches = re.findall(
            r"(?:grand total|amount payable|total amount|total)\s*[:#-]?\s*(?:₹|Rs\.?|INR)?\s*([0-9,]+(?:\.[0-9]{1,2})?)",
            text,
            re.IGNORECASE,
        )

        if total_matches:
            total = max(float(x.replace(",", "")) for x in total_matches)

        subtotal = max(total - gst, 0)

        items = self._extract_items(lines)

        if not items and subtotal > 0:
            items = [
                InvoiceItemBase(
                    description="Invoice Item",
                    quantity=1,
                    price=subtotal,
                    subtotal=subtotal,
                )
            ]

        confidence = 0.72

        if vendor != "Unknown Vendor":
            confidence += 0.05

        if invoice_number != "UNKNOWN":
            confidence += 0.05

        if total > 0:
            confidence += 0.08

        confidence = min(confidence, 0.95)

        return InvoiceExtraction(
            vendor_name=vendor,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            currency=currency,
            gst=gst,
            subtotal=subtotal,
            total=total,
            confidence_score=round(confidence, 2),
            items=items,
        )

    def _extract_items(self, lines):

        items = []

        pattern = (
            r"(.+?)\s+([0-9]+)\s+([0-9,]+(?:\.[0-9]{2})?)\s+([0-9,]+(?:\.[0-9]{2})?)$"
        )

        for line in lines:

            m = re.match(pattern, line)

            if not m:
                continue

            desc, qty, price, subtotal = m.groups()

            if len(desc) < 3:
                continue

            items.append(
                InvoiceItemBase(
                    description=desc,
                    quantity=float(qty),
                    price=float(price.replace(",", "")),
                    subtotal=float(subtotal.replace(",", "")),
                )
            )

        return items[:15]

    def _first_match(self, text, patterns, default):

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)

            if match:
                return match.group(1)

        return default