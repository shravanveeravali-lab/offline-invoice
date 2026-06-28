# Developer Guide

## Backend

- Entry point: `backend/app/main.py`
- Database models: `backend/app/models.py`
- OCR service: `backend/app/services/ocr.py`
- Local LLM service: `backend/app/services/llm.py`
- Storage service: `backend/app/services/storage.py`

## Frontend

- Entry point: `frontend/src/main.tsx`
- Dashboard: `frontend/src/App.tsx`
- API client: `frontend/src/api.ts`

## Testing

```powershell
cd backend
pytest

cd ..\frontend
npm test
npm run build
```

## Local Model Integration

The backend checks `LLAMA_CPP_BIN` and `TINYLLAMA_GGUF_PATH`. If both paths exist, it invokes llama.cpp with a compact JSON extraction prompt. If the model is unavailable or returns invalid JSON, the deterministic parser keeps the demo functional offline.
