from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Capstone API"
    DATABASE_URL: str = "sqlite:///./app.db"
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
