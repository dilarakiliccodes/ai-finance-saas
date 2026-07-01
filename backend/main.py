from fastapi import FastAPI

app = FastAPI(
    title="AI Finance SaaS API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "AI Finance SaaS Backend is Running 🚀"
    }