from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Sentiment Analyzer"

    class Config:
        env_file = ".env"

settings = Settings()
