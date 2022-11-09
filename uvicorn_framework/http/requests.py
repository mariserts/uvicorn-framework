import uuid
import urllib

from .. import constants

from ..conf import settings
from ..cryptography import hash_value


class Request:

    encoding = 'utf-8'

    __body = None
    __cookies = None

    def __init__(self, scope, body):
        self.id = uuid.uuid4().hex
        self._scope = scope
        self._body = body
        self._settings = settings

    @property
    def body(self):

        if self.__body is not None:
            return self.__body

        body = b''

        if self.method == 'post':
            body = self._body
        elif self.method == 'get':
            body = self._scope['query_string']

        decoded_body = body.decode(self.encoding, 'strict')
        clean_string = urllib.parse.unquote(decoded_body)

        out = {}

        for value in clean_string.split('&'):
            if '=' in value:
                parts = value.split('=')
                out[parts[0]] = parts[1]

        self.__body = out

        return self.__body

    @property
    def headers(self):

        _headers = self._scope['headers']

        headers = {}

        for header in _headers:
            key = header[0].decode('utf-8')
            value = header[1].decode('utf-8')
            headers[key] = value

        return headers

    @property
    def method(self):
        return self._scope['method'].lower()

    @property
    def cookies(self):

        if self.__cookies is not None:
            return self.__cookies

        value = self.headers.get('cookie', '')
        _cookies = value.split(';')

        cookies = {}

        for cookie in _cookies:
            if '=' in cookie:
                parts = cookie.split('=')
                cookies[parts[0].strip()] = parts[1].strip()

        self.__cookies = cookies

        return self.__cookies

    @property
    def path(self):
        return self._scope['path']

    @property
    def settings(self):
        return self._settings

    @property
    def type(self):
        return self._scope['type']

    @property
    def csrf_token(self):
        return self.cookies.get(
            constants.COOKIE_NAME_CSRF_TOKEN,
            self.get_csrf_token()
        )

    def get_csrf_token(self):
        return hash_value(self.id)

    def get_form_csrf_token(self):
        return hash_value(self.csrf_token)
