# REST API Documentation

Base URL: `http://127.0.0.1:8000`

## POST /upload

Uploads a PDF, image, or text invoice sample.

Response:

```json
{
  "filename": "invoice.pdf",
  "stored_path": "data/uploads/generated.pdf"
}
```

## POST /extract

Runs OCR, text cleaning, local extraction, validation, and SQLite persistence.

Request:

```json
{
  "stored_path": "data/uploads/generated.pdf"
}
```

Response: invoice JSON with database `id`.

## GET /invoice/{id}

Returns one persisted invoice.

## GET /history

Returns recent invoices. Optional query parameter: `q`.

## DELETE /invoice/{id}

Deletes an invoice, its items, and processing logs.
