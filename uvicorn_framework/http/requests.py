class Request:

    def __init__(self, scope, settings):
        self._scope = scope
        self._settings = settings

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
    def path(self):
        return self._scope['path']

    @property
    def settings(self):
        return self._settings

    @property
    def type(self):
        return self._scope['type']
