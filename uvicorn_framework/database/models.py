from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Model(Base):

    __abstract__ = True

    CASCADE_ALL = 'all'
    CASCADE_DELETE = 'delete'
    CASCADE_DELETE_ORPHAN = 'delete-orphan'
    CASCADE = f'{CASCADE_ALL}, {CASCADE_DELETE}, {CASCADE_DELETE_ORPHAN}'
