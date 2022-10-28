from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Model(Base):

    __abstract__ = True

    CASCADE_REMOVE_ALL = 'all, delete, delete-orphan'
