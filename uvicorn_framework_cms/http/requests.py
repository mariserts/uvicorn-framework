from uvicorn_framework.http.requests import Request as UFRequest

from ..database.models import Session, User


class Request(UFRequest):

    USER_UNSET_VALUE = 'unset'

    __user = str(USER_UNSET_VALUE)

    @property
    def user(self):
        if self.__user != self.USER_UNSET_VALUE:
            return self.__user
        self.__user = get_request_user()
        return self.__user

    def get_request_user(self):

        session_id = self.cookies.get(
            self.settings.SESSION_COOKIE_NAME,
            None
        )

        if session_id is None:
            return None

        session = self.settings.DB_ENGINE.cursor.query(Session).filter(
            id=session_id
        ).first()

        if session is None:
            return None

        return self.settings.DB_ENGINE.cursor.query(User).filter(
            id=session.user_id
        ).first()
