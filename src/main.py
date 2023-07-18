import time
from datetime import datetime

from sqlalchemy import insert, select, func
from sqlalchemy.orm import Session
from src.schemas import GeneratedData
from src.connect_db import engine

from loguru import logger
from faker import Faker

fake = Faker()

MAX_OBJECTS_QUERY = 30


class DatabaseUpdateSession:

    def new_data(self) -> dict:
        data = {
            'data': fake.bothify(text='????-########'),
            'date': datetime.now(),
        }

        logger.info(f'data is being transmitted -> {data}')
        return data

    def add_obj(self, data):
        stmt = (
            insert(GeneratedData).
            values(data=data.get('data'), date=data.get('date')).
            returning(GeneratedData)
        )
        return self.get_session(stmt, True)

    def get_all_obj(self):
        stmt = select(GeneratedData)
        return self.get_session(stmt)

    def get_count_obj(self):
        stmt = select(func.count()).select_from(GeneratedData)
        return self.get_session(stmt)

    def get_session(self, stmt, create=False):
        with Session(engine) as session:
            if create is False:
                return session.scalars(stmt).all()
            query = session.execute(stmt)
            return query.scalars().all()

    def script(self) -> None:
        while True:
            data = self.new_data()

            self.add_obj(data)
            logger.info(f'data recorded')

            count_obj = self.get_count_obj()[0]
            logger.info(f'there are {count_obj} objects in the database')

            if count_obj >= MAX_OBJECTS_QUERY:
                logger.warning(f'data deleted')

            time.sleep(1)



def main() -> None:
    scr = DatabaseUpdateSession()
    scr.script()


if __name__ == '__main__':
    main()
