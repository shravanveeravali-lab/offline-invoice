# Offline Usage Guide

1. Install all dependencies while online.
2. Install Tesseract OCR and Poppler.
3. Build or download llama.cpp.
4. Download a TinyLlama GGUF model from an open-source model host before the demo.
5. Set `LLAMA_CPP_BIN` and `TINYLLAMA_GGUF_PATH` in `backend/.env`.
6. Disable Wi-Fi.
7. Start `uvicorn app.main:app --host 127.0.0.1 --port 8000`.
8. Start `npm run dev` from `frontend/`.
9. Upload files from `samples/` or local invoice images.

The system must not call OpenAI, Gemini, Claude, Anthropic, Groq, or any remote AI endpoint.
