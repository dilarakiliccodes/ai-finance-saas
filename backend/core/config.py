from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Finance SaaS API"
    APP_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./ai_finance.db"

    class Config:
        env_file = ".env"

settings = Settings()
