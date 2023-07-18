from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

BaseModel = declarative_base()


class GeneratedData(BaseModel):

    __tablename__ = 'generated_data'

    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    data = Column(String(128), comment='Сгенерированая строка')
    date = Column(Date, comment='Дата создания')
