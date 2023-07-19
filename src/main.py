import time
from datetime import datetime
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from setting import settings
from schemas import GeneratedData
from connect_db import engine
from loguru import logger
from faker import Faker

fake = Faker()

MAX_OBJECTS_QUERY = settings.MAX_OBJECTS_QUERY


class DataControl:

    def __init__(self):
        self.session = self.get_session()

    def new_data(self) -> dict:
        data = GeneratedData(
            data=fake.bothify(text='????-########'),
            date=datetime.now(),
        )

        logger.info(
            f'data is being transmitted -> {data.data} {data.date}'.upper()
        )

        return data

    def add_obj(self, data):
        try:
            self.session.add(data)
            self.session.commit()
            logger.info(f'data recorded'.upper())

        except Exception as error:
            logger.error(f'no data recorded - {error}'.upper())
            self.session.rollback()

    def get_all_obj(self):
        stmt = select(GeneratedData)
        query = self.session.execute(stmt)
        return query.scalars().all()

    def get_count_obj(self):
        stmt = select(func.count()).select_from(GeneratedData)
        query = self.session.execute(stmt)
        count = query.scalars().first()
        logger.info(f'{count} objects in the database'.upper())
        return count

    def clean(self):
        try:
            self.session.query(GeneratedData).delete()
            self.session.commit()
        except Exception as error:
            logger.error(f'the data is not cleared - {error}'.upper())
            self.session.rollback()

    def is_max_data(self, count):
        if count >= MAX_OBJECTS_QUERY:
            logger.warning(f'exceeded the maximum value of objects -> {count}')
            self.clean()
            logger.warning(f'data deleted')

    def get_session(self):
        with Session(engine) as session:
            return session


def main() -> None:
    control = DataControl()

    while True:
        data = control.new_data()
        control.add_obj(data)
        count_obj = control.get_count_obj()
        control.is_max_data(count_obj)
        time.sleep(2)


if __name__ == '__main__':
    main()
