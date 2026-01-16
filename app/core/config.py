from pydantic_settings import BaseSettings  # ✅ Pydantic 2.x
from pathlib import Path

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
