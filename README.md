# 🤖 AI Finance SaaS API

AI-powered financial analysis backend built with FastAPI.

## 🚀 Features

- 🔐 JWT Authentication
- 👤 User Registration & Login
- 🤖 OpenAI Financial Analysis
- 📊 Financial Income/Expense Analysis
- 🗄️ SQLAlchemy ORM
- 🐳 Docker Support
- 📖 Swagger API Documentation

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT
- OpenAI API
- Docker

## 📂 Project Structure


backend/
├── api/
├── core/
├── database/
├── models/
├── routers/
├── schemas/
├── services/
├── utils/


## ⚙️ Installation

bash
git clone https://github.com/dilarakiliccodes/ai-finance-saas.git

cd ai-finance-saas

pip install -r requirements.txt

uvicorn backend.main:app --reload


## 📖 API Documentation

After running the project:


http://127.0.0.1:8000/docs


## 🤖 AI Finance Analysis Endpoint

Example request:

json
{
    "income": 35000,
    "expense": 27000
}


Example response:

json
{
    "analysis": "Your expenses are under control. Consider investing your monthly savings."
}


## 📌 Future Improvements

- PostgreSQL
- Redis
- Celery
- CI/CD Pipeline
- Frontend Dashboard

---

Made with ❤️ using FastAPI & OpenAI.