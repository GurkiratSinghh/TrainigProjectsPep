<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Gradio-F97316?style=for-the-badge&logo=gradio&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>

# 🧑‍💼 Employee Attrition Predictor

> A **machine learning** system that predicts whether an employee will stay or leave — powered by a **Decision Tree** classifier with a **FastAPI** backend and a **Gradio** web UI.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 ML Prediction | Decision Tree classifier trained on employee behaviour data |
| 🖥️ Gradio UI | Interactive web interface with sliders and input fields |
| 🔌 REST API | `POST /predict` endpoint for programmatic access |
| ⚙️ Auto-Train | Model trains automatically on first run if no saved model exists |
| 💾 Model Persistence | Trained model is pickled and reused across restarts |

---

## 🏗️ Project Structure

```
employee-attrition-ml/
├── app/
│   ├── main.py          # FastAPI app & /predict endpoint
│   ├── model.py         # Training, saving & loading the Decision Tree
│   └── schema.py        # Pydantic request schema
├── model/               # Saved model (.pkl)
├── gradio_app.py        # Gradio web interface
├── run.py               # Launches both FastAPI + Gradio together
└── requirements.txt
```

---

## 🚀 Quick Start

```bash
# 1 · Install dependencies
pip install -r requirements.txt

# 2 · Launch the full system (API + Gradio UI)
python run.py
```

- **Gradio UI** → `http://localhost:7860`
- **FastAPI Docs** → `http://127.0.0.1:8000/docs`

---

## 📡 API Usage

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 30,
    "monthly_income": 28000,
    "years_at_company": 2,
    "job_satisfaction": 2,
    "work_life_balance": 2,
    "mess": 0
  }'
```

**Response**
```json
{ "prediction": "LEAVE ❌" }
```

---

## 🔧 How It Works

```
Input Features                     Model                    Output
─────────────                     ─────                    ──────
Age                          ┌──────────────┐
Monthly Income          ───▶ │ Decision Tree│ ───▶   STAY ✅ / LEAVE ❌
Years at Company             │  (max_depth=4)│
Job Satisfaction             └──────────────┘
Work-Life Balance
```

---

## 🛠️ Tech Stack

- **scikit-learn** — Decision Tree classifier
- **FastAPI** — REST API serving predictions
- **Gradio** — interactive prediction UI
- **NumPy** — numerical processing
- **Uvicorn** — ASGI server

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
