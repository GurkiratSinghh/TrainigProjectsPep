<p align="center">
  <img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
  <img src="https://img.shields.io/badge/Gradio-F97316?style=for-the-badge&logo=gradio&logoColor=white" />
  <img src="https://img.shields.io/badge/Google%20Sheets-34A853?style=for-the-badge&logo=google-sheets&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>

# 🤖 Google Sheets LLM Chat

> An AI chatbot powered by **TinyLlama 1.1B** running on CPU with a **Gradio** web UI — every conversation is auto-logged to Google Sheets via OAuth.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧠 Local LLM | TinyLlama-1.1B-Chat running locally — no API keys needed for inference |
| 💬 Chat UI | Gradio-based conversational interface with chat history |
| 📊 Sheet Logging | Every user + bot message is appended to a Google Sheet in real time |
| 🔐 OAuth Login | Google OAuth 2.0 flow so users authenticate before accessing sheets |
| 🚀 HF Spaces Ready | Designed to deploy directly on Hugging Face Spaces |

---

## 🏗️ Project Structure

```
googlesheet_llm/
├── app.py               # Full application — LLM, OAuth, Gradio UI
├── client_secret.json   # Google OAuth credentials (not committed)
└── requirements.txt
```

---

## 🚀 Quick Start

```bash
# 1 · Install dependencies
pip install -r requirements.txt

# 2 · Set up Google OAuth
#     Create credentials at console.cloud.google.com
#     Update client_id & client_secret in app.py

# 3 · Launch
python app.py
```

The Gradio UI will open at `http://localhost:7860`.

---

## 🔧 How It Works

```
User Message
    ↓
TinyLlama (local inference on CPU)
    ↓
Bot Response displayed in Gradio chat
    ↓
Conversation logged → Google Sheets API
```

1. **Authentication** — User clicks "Login with Google" to authorize Sheets access
2. **Chat** — Messages are sent to the locally loaded TinyLlama model
3. **Logging** — Each exchange (`USER: ... | BOT: ...`) is appended to a configured spreadsheet

---

## 🛠️ Tech Stack

- **TinyLlama 1.1B** — lightweight causal LM from Hugging Face
- **Transformers + PyTorch** — model loading & inference
- **Gradio** — interactive chat UI
- **Google Sheets API v4** — conversation logging
- **google-auth-oauthlib** — OAuth 2.0 authentication flow

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
