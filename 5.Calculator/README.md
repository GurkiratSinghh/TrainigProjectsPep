<p align="center">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
</p>

# 🧰 Calc · Student · TextEditor — Multi-Tool Flask App

> Three handy tools bundled into a single **Flask** web application — a **right-to-left calculator**, a **text editor** with undo/redo, and a **student manager**.

---

## ✨ Features

| Tool | Route | Description |
|---|---|---|
| 🧮 Calculator | `/calc` | Stack-based right-to-left calculator with history |
| 📝 Text Editor | `/text` | Word-level editor with undo, redo & remove |
| 👨‍🎓 Student Manager | `/student` | Add, remove, and search students in a live list |

---

## 🏗️ Project Structure

```
Calculator/
├── app.py               # Flask app — routes for all three tools
├── calc.py              # RightToLeftCalc class (stack-based)
├── stktext.py           # SimpleTextEditor class (undo/redo stack)
├── student.py           # StudentManager class
├── static/
│   └── style.css        # Shared styles
├── templates/
│   ├── base.html        # Layout template
│   ├── calc.html        # Calculator UI
│   ├── text.html        # Text editor UI
│   └── student.html     # Student manager UI
└── README.md
```

---

## 🚀 Quick Start

```bash
# 1 · Install Flask
pip install flask

# 2 · Run the app
python app.py
# → http://127.0.0.1:5000
```

The home page auto-redirects to the **Calculator** — use the navbar to switch between tools.

---

## 🔧 How Each Tool Works

### 🧮 Calculator
- Push numbers and operators (`+`, `-`, `*`, `/`) onto a stack
- Evaluates right-to-left when enough operands are present
- Keeps a running history of past expressions

### 📝 Text Editor
- Add words one at a time
- **Undo** removes the last word • **Redo** restores it
- Displays the composed text in real time

### 👨‍🎓 Student Manager
- Add students by name (duplicates prevented)
- Remove or search for students
- Live list updates on every action

---

## 🛠️ Tech Stack

- **Flask** — lightweight Python web framework
- **Jinja2** — server-side HTML templating
- **HTML / CSS** — responsive frontend

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
