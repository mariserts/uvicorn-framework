from uvicorn_framework.conf import settings
from uvicorn_framework.http.requests import Request as UFRequest

from ..database.models import Session, User


class Request(UFRequest):

    USER_UNSET_VALUE = 'unset'

    __user = str(USER_UNSET_VALUE)

    @property
    def user(self):
        if self.__user != self.USER_UNSET_VALUE:
            return self.__user
        self.__user = self.get_request_user()
        return self.__user

    @property
    def session_token(self):
        return self.cookies.get(
            settings.SESSION_COOKIE_NAME,
            None
        )

    def get_request_user(self):

        cursor = settings.DB_ENGINE.cursor

        session_id = self.session_token
        if session_id is None:
            return None

        session = cursor.query(Session).filter_by(
            id=session_id
        ).first()

        if session is None:
            return None

        return cursor.query(User).filter_by(
            id=session.user_id
        ).first()
