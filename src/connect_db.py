from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schemas import BaseModel
from setting import settings

DB_PATH = (
    f'postgresql+psycopg2://'
    f'{settings.DB_USER}:'
    f'{settings.DB_PASS}@'
    f'{settings.DB_HOST}:'
    f'{settings.DB_PORT}'
    f'/postgres'
)

engine = create_engine(DB_PATH)


sessions = sessionmaker()
sessions.configure(bind=engine)
BaseModel.metadata.create_all(engine)
