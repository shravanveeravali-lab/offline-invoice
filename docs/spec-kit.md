# Spec Kit

## Project Vision

Build an offline, CPU-first document AI system that turns invoices, receipts, scans, and PDFs into validated accounting-ready JSON.

## Objectives

- Extract key invoice fields with no internet connection.
- Use free and open-source software only.
- Run on ordinary laptops without GPU acceleration.
- Provide a polished local dashboard for review and search.
- Store extracted data in SQLite for auditability.

## Target Users

- Small business owners
- Accountants
- Finance interns
- Offline field operators
- Hackathon judges evaluating local AI execution

## User Stories

- As an accountant, I can upload a scanned invoice and receive structured data.
- As a business owner, I can search prior invoices by vendor or invoice number.
- As a judge, I can disable Wi-Fi and still see OCR, extraction, storage, and dashboard features work.
- As a developer, I can run tests and quality checks locally.

## Functional Requirements

- Accept PDF and image invoices.
- Extract OCR text with Tesseract.
- Clean noisy OCR output.
- Generate structured invoice JSON.
- Persist invoices, items, and processing logs.
- Provide upload, extract, get, history, and delete APIs.
- Provide a dashboard for upload, search, and invoice review.

## Non-Functional Requirements

- Must run offline.
- Must use CPU inference.
- Must avoid CUDA and external AI APIs.
- Must provide real lint, test, build, and security checks.
- Must use AGPL-3.0-or-later licensing.

## Architecture

FastAPI handles uploads, OCR orchestration, extraction, and SQLite persistence. React consumes the REST API. Tesseract performs OCR. llama.cpp runs TinyLlama GGUF locally when configured, with a deterministic offline parser fallback for MVP reliability.

## Database Design

- `invoices`: vendor, number, date, currency, tax, subtotal, total, confidence, raw OCR text.
- `invoice_items`: description, quantity, unit price, subtotal, invoice foreign key.
- `processing_logs`: stage, status, message, invoice foreign key.

## JSON Schema

See [json-schema.md](json-schema.md).

## Offline Constraints

- No cloud APIs.
- No remote model calls.
- Model files must be downloaded before the demo.
- Dependency installation must happen before Wi-Fi is disabled.
- Runtime hosts must bind to local loopback.

## CPU Optimization Strategy

- Use Tesseract OCR and llama.cpp CPU runtime.
- Cap prompt size and generation tokens.
- Prefer structured extraction prompts.
- Cache persisted results in SQLite.
- Keep image DPI moderate for PDF conversion.

## Risks

- OCR quality may drop for blurry photos.
- Local model output may require validation and fallback parsing.
- Large PDFs may be slow on low-end CPUs.
- Missing Tesseract or Poppler installation can block OCR.

## Success Metrics

- App runs with Wi-Fi disabled.
- Upload and extraction complete under 60 seconds for a one-page invoice.
- Extracted JSON validates against schema.
- At least 80 percent of sample invoice fields are correct.
- CI includes real lint, test, security, and build jobs.

## Future Improvements

- Vendor-specific field correction.
- Local embeddings for duplicate detection.
- CSV and accounting exports.
- Multi-language OCR packs.
- Offline packaged desktop distribution.
