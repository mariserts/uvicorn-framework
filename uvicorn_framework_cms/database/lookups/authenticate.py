from uvicorn_framework.conf import settings

from ...cryptography import password_matches

from ..models import SessionModel
from ..serializers.sessions import SessionSerializer

from .sessions import create_session, delete_session
from .users import create_user, get_user


def register(mail, password):
    return create_user(mail, password, False)


def sign_in(email, password):

    user = get_user(email=email)
    if user is None:
        raise Exception('User does not exist')

    if password_matches(password, user.password) is False:
        raise Exception('Credentials incorrect')

    return create_session(user_id=user.id)


def sign_out(id, user_id):
    delete_session(id=id, user_id=user_id)
