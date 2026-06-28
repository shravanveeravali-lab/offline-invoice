# Specification: Offline Invoice Intelligence System

## Problem Statement

Businesses receive invoices in inconsistent formats such as scanned PDFs, photographed receipts, and vendor-generated documents. Manually reading these files and entering invoice data into accounting systems is slow, repetitive, and prone to errors.

Many AI-based document extraction systems depend on cloud APIs, which can create privacy, cost, connectivity, and compliance concerns. This project solves the problem by extracting invoice information locally using CPU-friendly open-source technologies.

## Vision

Build a reliable offline invoice intelligence system that allows users to upload invoices, extract key fields, review structured JSON, and store invoice records without internet access or cloud AI dependencies.

## Objectives

- Extract structured invoice data from images and PDFs.
- Run OCR and AI inference locally on CPU.
- Avoid all external AI APIs and internet runtime dependencies.
- Store results in SQLite for local search and auditability.
- Provide a clean dashboard for upload, review, and history.
- Demonstrate offline execution during the hackathon.
- Maintain professional documentation suitable for GitLab review.

## Scope

### In Scope

- Invoice image upload.
- Invoice PDF upload.
- OCR using Tesseract.
- Text cleaning after OCR.
- Local AI extraction using TinyLlama GGUF through llama.cpp.
- Structured JSON generation.
- SQLite persistence.
- Invoice history and search.
- Dashboard for review.
- Offline setup documentation.

### Out of Scope

- Cloud AI APIs.
- Online OCR services.
- GPU or CUDA inference.
- Payment processing.
- Direct accounting software synchronization in the first version.
- Multi-user cloud deployment.

## Target Users

- Small business owners
- Accountants
- Finance teams
- Hackathon judges
- Students demonstrating offline AI systems
- Organizations handling sensitive invoice data

## Functional Requirements

| ID | Requirement |
| -- | ----------- |
| FR-001 | Users can upload invoice images. |
| FR-002 | Users can upload invoice PDFs. |
| FR-003 | The system extracts text using local Tesseract OCR. |
| FR-004 | The system cleans OCR text before AI processing. |
| FR-005 | The system uses local TinyLlama GGUF through llama.cpp for invoice structuring. |
| FR-006 | The system produces structured JSON output. |
| FR-007 | The system stores invoice records in SQLite. |
| FR-008 | The system stores invoice line items separately. |
| FR-009 | The system records processing logs. |
| FR-010 | Users can view invoice history. |
| FR-011 | Users can search invoice history. |
| FR-012 | Users can retrieve a specific invoice. |
| FR-013 | Users can delete invoice records. |
| FR-014 | The system displays confidence scoring. |

## Non Functional Requirements

| ID | Requirement |
| -- | ----------- |
| NFR-001 | The application must run fully offline after setup. |
| NFR-002 | The application must use CPU-only inference. |
| NFR-003 | The application must not use cloud AI APIs. |
| NFR-004 | The application must use free and open-source software. |
| NFR-005 | The repository must use AGPL-3.0 licensing. |
| NFR-006 | The system should work on standard laptops without dedicated GPUs. |
| NFR-007 | Data should remain on the local machine. |
| NFR-008 | The system should provide clear error messages for missing OCR/model dependencies. |
| NFR-009 | The project should include professional documentation and GitLab-ready planning artifacts. |

## User Stories

- As an accountant, I want to upload an invoice PDF so that I can extract invoice details without manual entry.
- As a small business owner, I want the system to run offline so that sensitive invoice data stays on my laptop.
- As a finance team member, I want to search invoice history so that I can quickly find vendor records.
- As a hackathon judge, I want to disable Wi-Fi and still see the full pipeline work.
- As a developer, I want clear architecture and setup documentation so that I can maintain the project.

## Success Criteria

- The system accepts invoice images and PDFs.
- OCR runs locally using Tesseract.
- Local AI extraction runs through llama.cpp and TinyLlama GGUF.
- Extracted output includes vendor name, invoice number, date, currency, GST, items, subtotal, total, and confidence score.
- Records persist in SQLite.
- The dashboard supports upload, review, and history.
- The application runs with Wi-Fi disabled.
- Repository documentation satisfies Phase 1 hackathon requirements.

## Constraints

- No OpenAI, Gemini, Anthropic, Claude, Groq, or other cloud AI services.
- No internet dependency at runtime.
- No CUDA or GPU inference.
- Must use open-source software.
- Must use AGPL-3.0 license.
- Must be practical for laptop CPU execution.

## Assumptions

- Users will install Tesseract OCR before running the application.
- Users will download the TinyLlama GGUF model before offline execution.
- Input invoices are reasonably legible.
- Users will run the application on a local machine.
- SQLite is sufficient for MVP-scale local storage.

## Risks

| Risk | Impact | Mitigation |
| ---- | ------ | ---------- |
| Poor scan quality | Incorrect OCR output | Provide preprocessing guidance and confidence scoring |
| Missing Tesseract installation | OCR failure | Document setup and validate dependencies |
| Local LLM returns invalid JSON | Extraction failure | Validate output and use fallback parsing |
| Large PDFs are slow on CPU | Poor demo experience | Recommend single-page or compressed samples |
| Model file unavailable offline | AI extraction blocked | Download and configure model before demo |

## Acceptance Criteria

- A user can upload a supported invoice file.
- The system extracts text locally.
- The system generates structured JSON locally.
- The system stores the invoice and items in SQLite.
- The user can view invoice history.
- The user can search records.
- The project can be demonstrated without internet access.
- Documentation includes specification, plan, research, data model, tasks, README, governance files, roadmap, architecture, and GitLab issues.
