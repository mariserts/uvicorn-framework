from ..models import Session

from .users import get_user, password_matches


def sign_in(cursor, email, password):

    user = get_user(cursor, email)

    if user is None:
        return None

    if password_matches(password, user.password) is False:
        raise Exception('Credentials incorrect')

    session = Session(user_id=user.id)

    cursor.add(session)
    cursor.commit()

    return session


def sign_out(cursor, id, user_id):
    session = cursor(Session).filter(id=id, user_id=user_id).fist()
    if session is None:
        raise Exception('Session not found')
    session.delete(session)
    session.commit()
