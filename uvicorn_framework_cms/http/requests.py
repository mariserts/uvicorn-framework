from uvicorn_framework.conf import settings
from uvicorn_framework.http.requests import Request as UFRequest

from ..database.lookups.sessions import get_session
from ..database.lookups.users import get_user


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

        session_id = self.session_token
        if session_id is None:
            return None

        session = get_session(id=session_id)

        if session is None:
            return None

        return get_user(id=session.user_id)
