import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_NAME = os.getenv('DB_NAME', default='postgres')
    DB_USER = os.getenv('POSTGRES_USER', default='postgres')
    DB_PASS = os.getenv('POSTGRES_PASSWORD', default='postgres')
    DB_HOST = os.getenv('DB_HOST', default='localhost')
    DB_PORT = os.getenv('DB_PORT', default=5432)

    class Config:
        env_file = '.env'
        env_nested_delimiter = '__'


settings = Settings()
