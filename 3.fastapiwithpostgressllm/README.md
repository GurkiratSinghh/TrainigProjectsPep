<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
</p>

# 📚 LMS — Student Management API

> An industry-grade **Learning Management System** CRUD API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy** — plus a Flask-powered frontend for managing students.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📝 Full CRUD | Create, Read, Update, Delete students with validation |
| 🗃️ PostgreSQL | Persistent relational storage with auto-created tables |
| 🔒 Soft Delete | Records are soft-deleted by default; hard delete available |
| 📧 Email Uniqueness | Duplicate email prevention at the API level |
| 📖 Swagger Docs | Auto-generated interactive API docs at `/docs` |
| 🖥️ Flask Frontend | Web UI for managing student records |

---

## 🏗️ Project Structure

```
fastapiwithpostgressllm/
├── main.py              # FastAPI app — models, schemas, endpoints
├── flask_frontend/      # Flask web interface
│   ├── app.py
│   └── templates/
└── requirements.txt
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/students/` | Create a new student |
| `GET` | `/students/` | List students (pagination + status filter) |
| `GET` | `/students/{id}` | Get a single student |
| `PUT` | `/students/{id}` | Update student details |
| `DELETE` | `/students/{id}` | Soft delete a student |
| `DELETE` | `/students/{id}/hard` | Permanently delete a student |

---

## 🚀 Quick Start

```bash
# 1 · Install dependencies
pip install fastapi uvicorn sqlalchemy pydantic psycopg2-binary "pydantic[email]"

# 2 · Set up PostgreSQL
#     Update DATABASE_URL in main.py with your credentials

# 3 · Run the API
python main.py
# → http://127.0.0.1:8000/docs
```

---

## 🛠️ Tech Stack

- **FastAPI** — async REST API framework
- **PostgreSQL** — relational database
- **SQLAlchemy** — ORM with auto-migration
- **Pydantic v2** — request/response validation
- **Flask** — frontend web interface
- **Uvicorn** — ASGI server

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
