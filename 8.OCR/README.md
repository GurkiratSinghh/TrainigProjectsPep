<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Tesseract-4285F4?style=for-the-badge&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>

# 🪪 DL OCR Comparison System

> Upload a **Driving License** image and compare two OCR approaches side-by-side — **Tesseract (traditional)** vs. **Vision Language Model (VLM via HF API)** — with accuracy metrics and field-level scoring.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 Dual OCR | Tesseract (traditional) vs. VLM (Hugging Face Inference API) |
| 📊 Accuracy Scoring | Field-by-field accuracy comparison against ground truth |
| 🖼️ Image Preprocessing | Auto-enhances images before OCR for better results |
| 📈 Statistics Dashboard | Aggregate accuracy stats across all processed images |
| 🗃️ Result History | Browse, view, and delete past OCR results |
| 🌐 Web Frontend | Clean HTML/JS interface for uploading and reviewing |

---

## 🏗️ Project Structure

```
OCR/
├── main.py              # FastAPI app — upload, process, results endpoints
├── ocr_engines.py       # Tesseract & VLM engine implementations
├── utils.py             # Image preprocessing, accuracy calculator, field formatting
├── database.py          # Async result storage (SQLite)
├── download_models.py   # Model download helper
├── test_ocr.py          # Test suite
├── frontend/            # HTML/JS/CSS web interface
├── samples/             # Sample DL images for testing
├── results/             # Stored OCR results
└── requirements.txt
```

---

## 🚀 Quick Start

```bash
# 1 · Install dependencies
pip install -r requirements.txt

# 2 · Install Tesseract OCR engine
#     Windows: choco install tesseract
#     macOS:   brew install tesseract
#     Linux:   sudo apt install tesseract-ocr

# 3 · (Optional) Set HuggingFace token for VLM
set HF_TOKEN=your_token_here

# 4 · Run the server
python main.py
# → http://localhost:8000
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/upload` | Upload a DL image for OCR processing |
| `GET` | `/results` | List all processed results |
| `GET` | `/results/{id}` | Get a specific result |
| `DELETE` | `/results/{id}` | Delete a result |
| `GET` | `/stats` | Aggregate accuracy statistics |
| `GET` | `/health` | Health check |

---

## 🔧 How It Works

```
📷 DL Image Upload
      ↓
┌─────────────────┐    ┌─────────────────┐
│   Approach 1    │    │   Approach 2    │
│   Tesseract     │    │   VLM (HF API)  │
│   (Traditional) │    │   (AI Vision)   │
└────────┬────────┘    └────────┬────────┘
         ↓                      ↓
    Extracted Fields       Extracted Fields
         ↓                      ↓
    ┌────────────────────────────┐
    │   Accuracy Comparison     │
    │   (vs. Ground Truth)      │
    └───────────┬───────────────┘
                ↓
         📊 Results + Winner
```

**Extracted Fields**: Name, DOB, License Number, Issue/Expiry Dates, Address, Blood Group, Vehicle Class

---

## 🛠️ Tech Stack

- **FastAPI** — async API framework
- **Pytesseract** — traditional OCR engine
- **Hugging Face Inference API** — vision language model
- **OpenCV** — image preprocessing
- **SQLite (aiosqlite)** — async result storage
- **Uvicorn** — ASGI server

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
