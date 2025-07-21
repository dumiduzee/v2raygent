from decouple import config
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SUPABASE_URL:str = config("SUPABASE_URL")
    SUPABASE_KEY:str = config("SUPABASE_KEY")




setting = Settings()