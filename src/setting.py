from decouple import config
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SUPABASE_URL:str = config("SUPABASE_URL")
    SUPABASE_KEY:str = config("SUPABASE_KEY")
    JWT_TOKEN_EXPIRES_IN:int = config("JWT_TOKEN_EXPIRES_IN")
    JWT_ALGORITHM:str = config("JWT_ALGORITHM")
    JWT_SECRET_KEY:str = config("JWT_SECRET_KEY")
    MARZBAN_API_URL:str = config("MARZBAN_API_URL")
    MARZBAN_USERNAME:str = config("MARZBAN_USERNAME")
    MARZBAN_PASSWORD:str = config("MARZBAN_PASSWORD")




setting = Settings()