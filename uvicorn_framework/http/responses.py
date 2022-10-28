class Response:

    encoding = 'utf-8'
    default_headers = [
        [
            b'content-type',
            b'text/plain; charset=utf-8'
        ]
    ]

    def __init__(self, request, content, status=200, headers={}):
        self._request = request
        self._content = content
        self._status = status
        self._headers = headers

    @property
    def content(self):
        return self._content

    @property
    def headers(self):
        headers = self.default_headers
        for key, value in self._headers.items():
            headers.append([
                key.encode('utf-8', 'strict'),
                value.encode('utf-8', 'strict')
            ])
        return headers

    @property
    def request(self):
        return self._request

    @property
    def status(self):
        return self._status

    # --

    @property
    def start(self):
        return {
            'type': 'http.response.start',
            'status': self.status,
            'headers': self.headers,
        }

    @property
    def body(self):
        return {
            'type': 'http.response.body',
            'body': self.get_body(),
        }

    # --

    def get_body(self):
        return str.encode(self.content, self.encoding)


class RedirectResponse(Response):

    def __init__(self, url, permanent=False):
        self._url = url
        self._permanent = permanent
        self._status = 302
        if self._permanent is True:
            self._status = 301

        headers = {
            'location': url
        }

        super().__init__(None, '', status=self._status, headers=headers)


class TemplateResponse(Response):

    encoding = 'utf-8'
    default_headers = [
        [
            b'content-type',
            b'text/html; charset=utf-8'
        ]
    ]

    def __init__(self, request, template, status=200, headers={}, context={}):
        self._template = template
        self._context = context
        super().__init__(request, '', status=status, headers=headers)

    @property
    def context(self):
        return self._context

    @property
    def template(self):
        return self._template

    @property
    def content(self):
        template_engine = self.request.settings.TEMPLATE_ENGINE
        return template_engine.render(self.template, self.context)


class NotFoundResponse(Response):

    def __init__(self):
        super().__init__(None, 'Not found', status=404)


class NotImplementedResponse(Response):

    def __init__(self, content='Method not implemented'):
        super().__init__(None, content, status=501)


class ServerErrorResponse(Response):

    def __init__(self, content='Server error'):
        super().__init__(None, content, status=500)
