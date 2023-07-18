import time
from datetime import datetime

from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from src.schemas import GeneratedData
from src.connect_db import engine

from loguru import logger
from faker import Faker

fake = Faker()

MAX_OBJECTS_QUERY = 30


class DatabaseUpdateSession:

    def add_obj(self, data):
        stmt = (
            insert(GeneratedData).
            values(data=data.get('data'), date=data.get('date'))
        ).returning(GeneratedData)
        self.recordinc(stmt)

    def get_all_obj(self):
        stmt = select(GeneratedData)
        self.recordinc(stmt)


    def recordinc(self, stmp):
        with Session(engine) as session:
            obj = session.scalars(stmp).all()


    def script(self) -> None:
        while True:
            data = dict()
            data['data'] = fake.bothify(text='????-########')
            data['date'] = datetime.now()
            logger.info(f'data is being transmitted -> {data}')

            self.add_obj(data)
            logger.info(f'data recorded')

            all_data = self.get_all_obj()
            logger.warning(f'there are {all_data} objects in the database')
            #
            # if all_data.count() >= MAX_OBJECTS_QUERY:
            #     all_data.delete()
            #     all_data.commit()
            #     logger.warning(f'data deleted')
            # time.sleep(5)
            break


def main() -> None:
    scr = DatabaseUpdateSession()
    scr.script()


if __name__ == "__main__":
    main()



# def main() -> None:
#     while True:
#         data = dict()
#     data['data'] = fake.bothify(text='????-########')
#     data['date'] = datetime.now()
#     logger.info(f'data is being transmitted -> {data}')
#
#     stmt = insert(data)....
#
#     get_session(stmt)
#
#     self.session.add(new_data)
#     self.session.commit()
#     logger.info(f'data recorded')
#
#     all_data = self.session.query(GeneratedData)
#     logger.warning(f'there are {all_data.count()} objects in the database')
#
#     if all_data.count() >= MAX_OBJECTS_QUERY:
#         all_data.delete()
#         all_data.commit()
#         logger.warning(f'data deleted')
#     time.sleep(5)
#
#
# if __name__ == "__main__":
#     main()
#
#
# def get_session(query) -> Session:
#     with sessions() as session:
#         try:
#             t = session.execute(query)
#             return t.scalars().all()
#         except:
#             session.rollback()