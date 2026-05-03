# 🚀 Full-Stack-Task-Management-App-FastAPI-React-

TaskFlow is a **full-stack web application** built using **FastAPI (backend)** and **React (frontend)**.  
It provides user authentication and task management features with a clean, modern UI.

---

# 📌 Project Overview

TaskFlow helps users to:
- Register and login securely
- Create and manage tasks
- Track daily work efficiently
- Interact with a fast REST API backend

This project demonstrates **real-world full stack development skills** including API design, frontend integration, and authentication.

---

# ⚙️ Tech Stack

## 🟣 Frontend
- React.js
- TypeScript
- Vite
- Axios
- React Router

## 🔵 Backend
- FastAPI
- Python
- Pydantic
- SQLAlchemy (or in-memory DB for testing)
- JWT Authentication (optional upgrade)

---

# 📁 Project Structure


TaskFlow/
│
├── backend/
│ ├── src/
│ │ ├── api/
│ │ ├── core/
│ │ ├── models/
│ │ ├── schemas/
│ │ ├── services/
│ │ └── main.py
│
├── frontend/
│ ├── src/
│ │ ├── pages/
│ │ ├── api/
│ │ ├── components/
│ │ └── App.tsx
│
└── README.md


---

# 🚀 Features

## 🔐 Authentication
- User Registration
- User Login
- Backend validation

## 📝 Task Management
- Create tasks
- View all tasks
- Simple task storage system

## 🌐 Frontend Features
- React UI with components
- API integration using Axios
- Dynamic response display
- Clean dashboard UI

---

# 📡 API Endpoints

## 🔐 Auth APIs

### Register User

POST /auth/register


Request:
```json
{
  "email": "test@gmail.com",
  "password": "123456"
}

Response:

{
  "message": "User registered successfully",
  "email": "test@gmail.com"
}
Login User
POST /auth/login

Request:

{
  "email": "test@gmail.com",
  "password": "123456"
}

Response:

{
  "message": "Login successful"
}
📋 Task APIs
Get Tasks
GET /tasks/

Response:

[
  {
    "id": 1,
    "title": "My Task",
    "description": "Test task"
  }
]
Create Task
POST /tasks/

Request:

{
  "title": "My Task",
  "description": "Test task"
}

Response:

{
  "id": 1,
  "title": "My Task",
  "description": "Test task"
}
🚀 How to Run Project
🔵 Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn src.main:app --reload

Backend runs at:

http://127.0.0.1:8000
🟣 Frontend Setup
cd frontend
npm install
npm run dev

Frontend runs at:

http://localhost:5173
📸 UI OUTPUT
🔐 Login Output
🔐 Login Successful
Welcome test@gmail.com
📝 Register Output


📡 API Endpoints
Auth
POST /auth/register
POST /auth/login
Tasks
GET /tasks/
POST /tasks/
✅ User registered successfully
Email: test@gmail.com
📋 Task Output
📋 My Tasks
✔ Study FastAPI
✔ Build React UI
✔ Connect Backend

👨‍💻 Author

Ankita Baddoli
Python Full Stack Developer

⭐ Future Improvements
Docker deployment
PostgreSQL integration
CI/CD pipeline
Cloud deployment (Render / AWS)
