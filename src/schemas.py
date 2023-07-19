from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

BaseModel = declarative_base()


class GeneratedData(BaseModel):

    __tablename__ = 'free_entry'

    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    data = Column(String, comment='Сгенерированая строка')
    date = Column(DateTime, comment='Дата создания')
