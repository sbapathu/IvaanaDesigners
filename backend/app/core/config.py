from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Ivaana Designers"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "your-secret-key")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    JWT_ALGORITHM: str = "HS256"
    SERVER_NAME: str = os.environ.get("SERVER_NAME", "localhost")
    SERVER_HOST: str = os.environ.get("SERVER_HOST", "http://localhost:8000")
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:5173"]
    DB_URL: str = "postgresql://postgres:password@localhost:5432/ivaanadesigners"
    DB_USER_PWD: str = os.environ.get("DB_USER_PWD", "password")
    auto_create_tables: bool = True
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
settings = Settings()