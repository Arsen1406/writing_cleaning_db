from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schemas import BaseModel
from setting import settings


engine = create_engine(settings.DB_DSN)

sessions = sessionmaker()
sessions.configure(bind=engine)
BaseModel.metadata.create_all(engine)
