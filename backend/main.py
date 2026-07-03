from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.config import settings
from backend.database.connection import Base, engine
from backend.models.user import User
from backend.routers.user_router import router as user_router
from backend.routers.finance_router import router as finance_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(finance_router)


@app.get("/")
def home():
    return {
        "message": "AI Finance SaaS Backend is Running 🚀"
    }