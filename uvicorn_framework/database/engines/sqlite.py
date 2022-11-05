import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ...conf import settings

from .base import BaseDatabaseEngine


class SqliteDatabaseEngine(BaseDatabaseEngine):

    __engine = None
    __session = None

    filename = 'db.sqlite3'

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

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

        path = settings.DIR + '/' + self.filename

        if os.path.exists(path) is False:
            with open(path, 'x') as f:
                f.write('')

        return create_engine(
            f'sqlite:///{path}',
            echo=settings.DB_ECHO
        )

    def get_session(self):
        return sessionmaker(
            bind=self.engine,
            expire_on_commit=False
        )
