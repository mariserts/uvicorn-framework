class Request:

    __cookies = None

    def __init__(self, scope, settings):

        print(scope)

        self._scope = scope
        self._settings = settings

        print(self.cookies)

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
