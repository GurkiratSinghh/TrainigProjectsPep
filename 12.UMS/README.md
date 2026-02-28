<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Supabase-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
</p>

# 🎓 University Placement Portal

> A cloud-native **University Management System** focused on the **Placement & Career Services** workflow — with a **FastAPI** backend, **Supabase** database, and a **React + TypeScript** frontend.

---

## ✨ Features

| Module | Description |
|---|---|
| 🔐 Authentication | JWT-based auth with role-based access (Admin, Student, Recruiter) |
| 👨‍🎓 Student Profiles | Academic records, skills, resume management |
| 💼 Placements | Placement status tracking & offers |
| 🏢 Drives | Campus drive scheduling & management |
| 📄 Documents | Document upload & verification |
| 💬 Messaging | In-app communication between users |
| 🔔 Notifications | Real-time notification system |
| 👥 User Management | Admin panel for user CRUD |
| 📜 Audit Logs | Complete action audit trail |

---

## 🏗️ Project Structure

```
UMS/
├── backend/
│   └── app/
│       ├── main.py              # FastAPI entry point
│       ├── core/
│       │   └── config.py        # Settings & environment
│       ├── auth/                # Authentication router
│       ├── students/            # Student profiles
│       ├── placements/          # Placement tracking
│       ├── drives/              # Campus drive management
│       ├── documents/           # Document handling
│       ├── messaging/           # In-app messaging
│       ├── notifications/       # Notification system
│       ├── users/               # User management
│       ├── admin/               # Admin operations
│       └── audit/               # Audit logging
├── frontend/                    # React + TypeScript (Vite)
│   └── src/
├── insert_data.sql              # Seed data
└── supabase_schema.sql          # Full database schema
```

---

## 🚀 Quick Start

### Backend

```bash
cd backend

# 1 · Install dependencies
pip install -r requirements.txt

# 2 · Configure environment
#     Set SUPABASE_URL, SUPABASE_KEY, JWT_SECRET in .env

# 3 · Run the API
uvicorn app.main:app --reload
# → http://127.0.0.1:8000/api/docs
```

### Frontend

```bash
cd frontend
npm install
npm run dev
# → http://localhost:5173
```

### Database

```sql
-- Run in Supabase SQL Editor
-- 1. Create tables
\i supabase_schema.sql

-- 2. Seed test data
\i insert_data.sql
```

---

## 📡 API Overview

All endpoints are versioned under `/api/v1`:

| Module | Prefix | Key Operations |
|---|---|---|
| Auth | `/auth` | Register, Login, Refresh tokens |
| Students | `/students` | Profile CRUD, skill management |
| Placements | `/placements` | Track offers & placement status |
| Drives | `/drives` | Schedule & manage campus drives |
| Documents | `/documents` | Upload & verify documents |
| Messaging | `/messaging` | Send & receive messages |
| Notifications | `/notifications` | Notification management |
| Users | `/users` | Admin user operations |
| Admin | `/admin` | System administration |
| Audit | `/audit` | View audit logs |

---

## 🛠️ Tech Stack

- **FastAPI** — async REST API framework
- **Supabase (PostgreSQL)** — managed database + auth
- **React + TypeScript + Vite** — modern frontend
- **Pydantic v2** — data validation
- **JWT** — token-based authentication
- **Uvicorn** — ASGI server

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
