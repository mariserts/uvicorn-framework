from uvicorn_framework.conf import settings

from ..models import SessionModel
from ..serializers.sessions import SessionSerializer


Session = settings.DB_ENGINE.session


def create_session(
        user_id
    ):

    session = None

    with Session() as cursor:

        session = SessionModel(
            user_id=user_id,
        )

        cursor.add(session)
        cursor.commit()

        session = SessionSerializer(id=session.id, user_id=session.user_id)

    return session


def delete_session(
        id,
        user_id=None,
    ):

    with Session() as cursor:

        condition_kwargs = {
            'id': id
        }

        if user_id is not None:
            condition_kwargs['user_id'] = user_id

        session = cursor.query(SessionModel).filter_by(**condition_kwargs).first()
        if session is None:
            raise Exception('SessionModel not found')

        cursor.delete(session)
        cursor.commit()

    return


def get_session(
        id=None,
        user_id=None,
    ):

    session = None

    with Session() as cursor:

        condition_kwargs = {}

        if id is not None:
            condition_kwargs['id'] = id

        if user_id is not None:
            condition_kwargs['user_id'] = user_id

        session = cursor.query(SessionModel).filter_by(**condition_kwargs).first()

        if session is None:
            return None

        session = SessionSerializer(id=session.id, user_id=session.user_id)

    return session
