from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    OPENROUTER_API_KEY: str
    OPENROUTER_MODEL: str
    OPENROUTER_BASE_URL: str

    EMBEDDING_MODEL: str 
    GENERATION_MODEL: str
    EMBEDDING_DIMENSION: int
    
    DATABASE_URL:str
    VECTOR_STORE_PATH:str
    
    FASTAPI_HOST: str 
    FASTAPI_PORT: int 
    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()