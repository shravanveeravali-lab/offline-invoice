# Offline Invoice Intelligence System

## Problem Statement

Businesses receive invoices in different formats (PDFs, scanned images, photos). Manually entering invoice information into accounting software is time-consuming and error-prone.

This project extracts important invoice information completely offline using CPU-optimized AI models.

## Features

- Upload invoice PDF or image
- OCR using Tesseract
- Local AI extracts structured fields
- Store extracted data in SQLite
- Search previous invoices
- Works without internet
- CPU optimized

## Workflow

Invoice Image/PDF
↓
OCR (Tesseract)
↓
Text Cleaning
↓
Local Small Language Model
↓
Structured JSON
↓
SQLite Database

## Sample Output

{
  "invoice_number": "INV-1024",
  "vendor": "ABC Electronics",
  "date": "2026-06-27",
  "items": [
    {
      "name": "Keyboard",
      "quantity": 2,
      "price": 1200
    }
  ],
  "gst": 432,
  "total": 2832
}

## Tech Stack

Frontend
- React
- TypeScript

Backend
- FastAPI

AI
- Tesseract OCR
- llama.cpp
- TinyLlama GGUF

Database
- SQLite

Deployment
- Offline Local Desktop