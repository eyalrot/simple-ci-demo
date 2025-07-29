from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI POC"
    VERSION: str = "0.1.0"
    DEBUG: bool = True
    
    CORS_ORIGINS: List[str] = ["*"]
    
    DATABASE_URL: str = "sqlite:///./app.db"
    
    class Config:
        env_file = ".env"


settings = Settings()