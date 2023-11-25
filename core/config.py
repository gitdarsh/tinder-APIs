from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv(".env")

class Settings(BaseSettings):
    DB_URL : str

config = Settings(".env")