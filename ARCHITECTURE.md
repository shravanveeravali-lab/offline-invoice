# Architecture

## Overview

Offline Invoice Intelligence System is a local web application for extracting structured invoice data from images and PDFs. It uses a React TypeScript frontend, a FastAPI backend, Tesseract OCR, TinyLlama GGUF through llama.cpp, and SQLite.

The system is designed to run fully offline after setup. All OCR, AI inference, validation, and persistence happen on the user's machine.

## System Architecture

```mermaid
flowchart LR
    User[User] --> UI[React Dashboard]
    UI --> API[FastAPI REST API]
    API --> Upload[Local Upload Storage]
    API --> OCR[Tesseract OCR]
    OCR --> Clean[Text Cleaning]
    Clean --> LLM[llama.cpp Runtime]
    LLM --> Model[TinyLlama GGUF Model]
    LLM --> JSON[Structured JSON]
    JSON --> Validate[Validation Layer]
    Validate --> DB[(SQLite Database)]
    DB --> API
    API --> UI
```

## Component Responsibilities

| Component | Responsibility |
| --------- | -------------- |
| React Dashboard | Upload files, display extraction results, search invoice history |
| FastAPI Backend | Expose REST APIs and coordinate the extraction pipeline |
| Upload Storage | Keep source invoice files locally |
| Tesseract OCR | Extract text from invoice images and PDFs |
| Text Cleaning | Normalize OCR text before local AI processing |
| llama.cpp | Run the local TinyLlama GGUF model on CPU |
| TinyLlama GGUF | Convert cleaned OCR text into structured invoice JSON |
| Validation Layer | Ensure extracted fields match expected schema |
| SQLite | Store invoices, invoice items, and processing logs |

## Workflow

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant B as Backend
    participant O as Tesseract OCR
    participant L as llama.cpp + TinyLlama
    participant D as SQLite

    U->>F: Upload invoice file
    F->>B: POST /upload
    B-->>F: Stored file reference
    F->>B: POST /extract
    B->>O: Run local OCR
    O-->>B: OCR text
    B->>B: Clean text
    B->>L: Extract structured JSON locally
    L-->>B: Invoice JSON
    B->>B: Validate JSON
    B->>D: Save invoice, items, logs
    D-->>B: Stored record
    B-->>F: Extracted invoice response
    F-->>U: Display invoice details
```

## Database ER Diagram

```mermaid
erDiagram
    INVOICES ||--o{ INVOICE_ITEMS : contains
    INVOICES ||--o{ PROCESSING_LOGS : has

    INVOICES {
        integer id PK
        string vendor_name
        string invoice_number
        string invoice_date
        string currency
        decimal gst
        decimal subtotal
        decimal total
        decimal confidence_score
        string source_filename
        text raw_text
        datetime created_at
    }

    INVOICE_ITEMS {
        integer id PK
        integer invoice_id FK
        string description
        decimal quantity
        decimal price
        decimal subtotal
    }

    PROCESSING_LOGS {
        integer id PK
        integer invoice_id FK
        string stage
        string status
        text message
        datetime created_at
    }
```

## Folder Structure

```mermaid
flowchart TD
    A["offline-invoice-intelligence-system/"]
    A --> B["backend/"]
    A --> C["frontend/"]
    A --> D["specs/"]
    A --> E["docs/"]
    A --> F["samples/"]
    A --> G["README.md"]
    A --> H["ARCHITECTURE.md"]
    A --> I["ROADMAP.md"]
    D --> J["001-offline-invoice-intelligence/"]
    J --> K["spec.md"]
    J --> L["plan.md"]
    J --> M["research.md"]
    J --> N["data-model.md"]
    J --> O["tasks.md"]
```

## Offline Boundary

The offline boundary includes:

- Uploaded invoice files
- OCR processing
- Cleaned invoice text
- Local LLM inference
- Structured JSON validation
- SQLite persistence
- Dashboard review

The system must not cross the offline boundary by sending invoice data to external services.

## Deployment Model

The application is deployed locally:

- Frontend runs on localhost.
- Backend runs on localhost.
- SQLite runs as an embedded local database.
- Tesseract, Poppler, llama.cpp, and TinyLlama GGUF are installed locally.

## Quality Attributes

- Privacy: invoice data remains local.
- Portability: can run on laptops without GPU.
- Maintainability: clear component boundaries.
- Auditability: records and logs are stored in SQLite.
- Reliability: structured output is validated before persistence.
- Demonstrability: Wi-Fi can be disabled during demo.
