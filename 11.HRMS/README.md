<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Supabase-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>

# 🏢 HRMS — Human Resource Management System

> A comprehensive **Human Resource Management** backend covering **40 Supabase tables** across 16 HR domains — built with **FastAPI** and paired with a **React** frontend.

---

## ✨ Features

| Domain | Highlights |
|---|---|
| 👤 Employees | Full employee profiles, org hierarchy |
| 🏢 Departments | Department CRUD with manager assignments |
| 🕐 Attendance | Clock-in/out, shift management |
| 🏖️ Leave | Leave requests, approvals, balance tracking |
| 💰 Payroll | Salary structure, allowances, deductions, payslips |
| 📋 Recruitment | Job postings, applications, interview pipeline |
| 📊 Performance | Reviews, KPIs, goals, rating cycles |
| 🎓 Training | Programs, enrollments, skill tracking |
| 🏥 Benefits | Employee benefit plans |
| 🖥️ Assets | Company asset assignment & tracking |
| 💸 Reimbursements | Expense claims & approvals |
| 🔔 Notifications | In-app notification system |
| ⚖️ Disciplinary | Disciplinary action records |
| 🚪 Exit | Exit interviews & offboarding |
| 📜 Audit | Complete audit trail |
| 🔐 Auth | JWT authentication with role-based access |

---

## 🏗️ Project Structure

```
HRMS/
├── main.py              # FastAPI app — registers all 16 routers
├── database.py          # Supabase client setup
├── config.py            # Environment configuration
├── auth_table.sql       # SQL schema for auth tables
├── routes/
│   ├── auth.py          # Authentication & JWT
│   ├── employees.py     # Employee CRUD
│   ├── departments.py   # Department management
│   ├── attendance.py    # Attendance tracking
│   ├── leave.py         # Leave management
│   ├── payroll.py       # Salary & payslips
│   ├── recruitment.py   # Hiring pipeline
│   ├── performance.py   # KPIs & reviews
│   ├── training.py      # Training programs
│   ├── benefits.py      # Employee benefits
│   ├── assets.py        # Asset management
│   ├── reimbursements.py
│   ├── notifications.py
│   ├── disciplinary.py
│   ├── exit.py
│   └── audit.py
├── schemas/             # Pydantic request/response models
├── frontend/            # React (Vite) frontend
│   └── src/
├── render.yaml          # Render deployment config
├── DEPLOYMENT_GUIDE.md
└── requirements.txt
```

---

## 🚀 Quick Start

### Backend

```bash
# 1 · Install dependencies
pip install -r requirements.txt

# 2 · Configure Supabase
#     Set SUPABASE_URL and SUPABASE_KEY in .env or config.py

# 3 · Run the API
uvicorn main:app --reload
# → http://127.0.0.1:8000/docs
```

### Frontend

```bash
cd frontend
npm install
npm run dev
# → http://localhost:5173
```

---

## 🛠️ Tech Stack

- **FastAPI** — async REST API framework
- **Supabase (PostgreSQL)** — backend-as-a-service database
- **Pydantic v2** — data validation
- **React + Vite** — modern frontend
- **JWT** — token-based authentication
- **Uvicorn** — ASGI server

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
