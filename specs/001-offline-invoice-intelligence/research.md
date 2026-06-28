# Research: Offline Invoice Intelligence System

## OCR

Optical Character Recognition converts text in scanned documents, images, and PDFs into machine-readable text. Invoice OCR is challenging because invoices contain tables, varying vendor layouts, small fonts, stamps, logos, and inconsistent image quality.

OCR is required before local language-model extraction because invoices are often image-based rather than text-based. The OCR output becomes the intermediate representation used by the extraction model.

## Tesseract

Tesseract OCR is a mature, open-source OCR engine maintained by the community. It supports many languages, runs locally, and performs well on CPU. It is a strong fit for offline invoice extraction because it does not require a remote service.

### Why Tesseract Was Chosen

- Free and open source.
- Works fully offline.
- Runs on CPU.
- Supports many languages.
- Widely documented and widely used.
- Integrates well with Python backends.

### Limitations

- Accuracy depends on image quality.
- Complex tables may require post-processing.
- Very noisy scans may produce fragmented text.

## TinyLlama

TinyLlama is a compact open-source language model suitable for local experimentation and low-resource inference. For this project, TinyLlama is used to transform cleaned OCR text into structured invoice JSON.

### Why TinyLlama Was Chosen

- Small enough for laptop CPU use.
- Compatible with GGUF quantization.
- Suitable for constrained local demos.
- Avoids cloud AI dependencies.
- Good fit for hackathon-scale structured extraction.

### Limitations

- Less accurate than large cloud models.
- May require strict prompting and validation.
- May produce malformed JSON without safeguards.

## llama.cpp

llama.cpp is an efficient C/C++ runtime for running quantized language models locally. It supports GGUF models and is optimized for CPU inference, making it appropriate for offline AI applications.

### Why llama.cpp Was Chosen

- Runs locally without cloud services.
- Supports CPU-only inference.
- Supports quantized GGUF models.
- Has broad community adoption.
- Suitable for laptops without GPUs.

## SQLite

SQLite is an embedded relational database that stores data in a local file. It requires no database server and is ideal for offline applications.

### Why SQLite Was Chosen

- Works fully offline.
- Requires no separate service.
- Easy to back up and inspect.
- Supports relational tables for invoices and items.
- Reliable for local desktop-scale workloads.

## CPU Optimization

The application is designed for laptops without GPUs. CPU optimization focuses on minimizing OCR and LLM workload while preserving extraction quality.

### Strategies

- Use a small quantized GGUF model.
- Limit prompt size.
- Limit model output tokens.
- Clean OCR text before model inference.
- Store processed results in SQLite to avoid repeated extraction.
- Use Tesseract locally instead of heavier OCR models.
- Avoid CUDA-only dependencies.

## Offline AI

Offline AI means that inference runs entirely on the local machine. This improves privacy, reduces recurring API costs, and allows operation in low-connectivity environments.

### Benefits

- Sensitive invoice data stays local.
- No cloud billing.
- Demo works with Wi-Fi disabled.
- Lower compliance risk for financial documents.
- Predictable runtime dependencies after setup.

### Tradeoffs

- Smaller local models may be less accurate.
- CPU inference is slower than GPU/cloud inference.
- Users must install local dependencies and model files.

## Why These Technologies Were Chosen

| Technology | Reason |
| ---------- | ------ |
| React | Mature frontend framework for dashboards |
| TypeScript | Safer frontend development |
| Vite | Fast local development tooling |
| FastAPI | Clean REST APIs and Python ecosystem compatibility |
| Tesseract OCR | Open-source offline OCR |
| llama.cpp | CPU-friendly local LLM runtime |
| TinyLlama GGUF | Lightweight local model for extraction |
| SQLite | Embedded offline database |
| AGPL-3.0 | Strong copyleft license aligned with open-source rules |

## Alternatives Considered

| Alternative | Reason Not Selected |
| ----------- | ------------------- |
| OpenAI API | Violates offline and no-cloud requirements |
| Gemini API | Violates offline and no-cloud requirements |
| Claude API | Violates offline and no-cloud requirements |
| Cloud OCR services | Require internet and external processing |
| PostgreSQL | More operational overhead than needed for local MVP |
| Large LLMs | Too resource-heavy for CPU-only laptop execution |
| CUDA-based inference | Violates CPU-only constraint |
| Browser-only OCR | Less mature for PDF/image invoice workflow |
