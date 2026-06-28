# Roadmap

## Project Goal

Deliver a professional offline-first invoice intelligence system that runs on CPU-only laptops, extracts structured invoice data locally, and satisfies hackathon requirements for privacy, open-source tooling, and offline AI execution.

## Phase 1: Planning and Documentation

Status: Complete

- Project specification
- Architecture plan
- Research documentation
- Data model
- Task breakdown
- README
- Governance files
- GitLab issues
- Mermaid diagrams

## Phase 2: MVP Application

Status: In Progress

- Upload invoice images and PDFs
- Run Tesseract OCR locally
- Clean OCR text
- Extract structured JSON using TinyLlama GGUF through llama.cpp
- Store records in SQLite
- Display dashboard with history and search
- Provide local demo samples

## Phase 3: Offline Demo Readiness

Status: Planned

- Validate Wi-Fi-disabled execution
- Confirm local model path configuration
- Prepare sample invoices
- Record demo flow
- Add screenshots to README
- Confirm no external AI dependencies

## Phase 4: Accuracy and Reliability

Status: Planned

- Field-level confidence scoring
- Better table extraction
- Vendor-specific correction rules
- Duplicate invoice detection
- Improved PDF preprocessing
- Validation against invoice totals

## Phase 5: Packaging and Distribution

Status: Future

- Desktop packaging
- One-command local startup
- Offline installer checklist
- Export to CSV
- Export to accounting formats
- Local backup and restore

## Long-Term Opportunities

- Multilingual OCR support
- Local embedding search
- Template learning for recurring vendors
- Human-in-the-loop correction interface
- Batch invoice processing
- Local audit reports
