from uvicorn_framework.conf import settings

from ...cryptography import password_matches

from ..models import Session

from .users import create_user, get_user


def register(mail, password):
    return create_user(mail, password, False)


def sign_in(email, password):

    cursor = settings.DB_ENGINE.cursor

    user = get_user(email=email)
    if user is None:
        raise Exception('User does not exist')

    if password_matches(password, user.password) is False:
        raise Exception('Credentials incorrect')

    session = Session(user_id=user.id)

    cursor.add(session)

    cursor.commit()

    return session


def sign_out(id, user_id):

    cursor = settings.DB_ENGINE.cursor

    session = cursor.query(Session).filter_by(id=id, user_id=user_id).first()
    if session is None:
        raise Exception('Session not found')

    cursor.delete(session)

    cursor.commit()
