from pydantic_settings import BaseSettings , SettingsConfigDict
from functools import lru_cache

class APP_config(BaseSettings):
    app_name:str = "FASTAPI"
    app_env:str = "DEVELOPMENT"
    database_url:str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    
    model_config= SettingsConfigDict(env_file=".env")

@lru_cache 
def get_app_config():
    return APP_config()