# Resume Bullets

- Built a CPU-first offline Document AI system that extracts structured invoice data from PDFs and scanned receipts without cloud APIs.
- Integrated Tesseract OCR, llama.cpp, TinyLlama GGUF, FastAPI, React, TypeScript, and SQLite into a local web application.
- Designed an offline invoice extraction pipeline with OCR cleaning, schema validation, deterministic fallback parsing, and confidence scoring.
- Implemented REST APIs for upload, extraction, invoice history, search, lookup, and deletion.
- Created a SQLite data model for invoices, line items, and processing logs with searchable invoice history.
- Optimized the architecture for laptop CPU execution using compact prompts, local persistence, and lightweight services.
- Added production-style repository governance with AGPL licensing, CI, pre-commit, security scanning, and developer documentation.
