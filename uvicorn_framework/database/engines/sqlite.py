import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import DatabaseEngine


class SqliteDatabaseEngine(DatabaseEngine):

    __engine = None
    __session = None

    filename = 'db.sqlite3'

    @property
    def engine(self):
        if self.__engine is not None:
            return self.__engine
        self.__engine = self.get_engine()
        return self.__engine

    @property
    def session(self):
        return self.get_session()

    def get_engine(self):
        return create_engine(f'sqlite:///{self.filename}', echo=False)

    def get_session(self):
        return sessionmaker(bind=self.engine, expire_on_commit=False)

    def setup(self):

        path = self.settings.DIR + '/' + self.filename

        if os.path.exists(path) is False:
            with open(path, 'x') as f:
                f.write('')
