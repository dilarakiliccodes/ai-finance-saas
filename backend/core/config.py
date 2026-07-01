from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Finance SaaS API"
    APP_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./ai_finance.db"
    SECRET_KEY: str = "change-this-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
