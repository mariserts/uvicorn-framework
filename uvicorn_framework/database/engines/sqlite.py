import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import DatabaseEngine


class SqliteDatabaseEngine(DatabaseEngine):

    __cursor = None
    __engine = None
    __session = None

    filename = 'db.sqlite3'

    @property
    def cursor(self):
        if self.__cursor is not None:
            return self.__cursor
        Session = sessionmaker(bind=self.engine)
        self.__cursor = Session()
        return self.__cursor

    @property
    def engine(self):
        if self.__engine is not None:
            return self.__engine
        self.__engine = create_engine(f'sqlite:///{self.filename}', echo=True)
        return self.__engine

    def setup(self):

        path = self.settings.DIR + '/' + self.filename

        if os.path.exists(path) is False:
            with open(path, 'x') as f:
                f.write('')
