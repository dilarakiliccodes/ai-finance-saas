from fastapi import FastAPI
from backend.core.config import settings
from backend.database.connection import Base, engine
from backend.models.user import User

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

Base.metadata.create_all(bind=engine)
@app.get("/")
def home():
    return {
        "message": "AI Finance SaaS Backend is Running 🚀"
    }