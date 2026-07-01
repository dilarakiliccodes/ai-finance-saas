from fastapi import FastAPI
from backend.core.config import settings
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

@app.get("/")
def home():
    return {
        "message": "AI Finance SaaS Backend is Running 🚀"
    }