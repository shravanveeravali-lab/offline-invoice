# JSON Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "InvoiceExtraction",
  "type": "object",
  "required": ["vendor_name", "invoice_number", "invoice_date", "currency", "items", "subtotal", "total", "confidence_score"],
  "properties": {
    "vendor_name": { "type": "string" },
    "invoice_number": { "type": "string" },
    "invoice_date": { "type": "string" },
    "currency": { "type": "string" },
    "gst": { "type": "number", "minimum": 0 },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["description", "quantity", "price", "subtotal"],
        "properties": {
          "description": { "type": "string" },
          "quantity": { "type": "number", "minimum": 0 },
          "price": { "type": "number", "minimum": 0 },
          "subtotal": { "type": "number", "minimum": 0 }
        }
      }
    },
    "subtotal": { "type": "number", "minimum": 0 },
    "total": { "type": "number", "minimum": 0 },
    "confidence_score": { "type": "number", "minimum": 0, "maximum": 1 }
  }
}
```
