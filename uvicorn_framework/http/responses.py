from ..conf import settings


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
        self._headers = self.parse_headers(headers)

    @property
    def content(self):
        return self._content

    @property
    def headers(self):
        return self._headers

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

    def parse_headers(self, headers_dict):

        headers = []
        headers += self.get_default_headers()

        for key, value in headers_dict.items():
            headers.append([
                key.encode('utf-8', 'strict'),
                value.encode('utf-8', 'strict')
            ])

        return headers

    # --

    def set_cookie(
            self,
            key,
            value,
            max_age=None,
            expires=None,
            domain=None,
            path='/',
            secure=True,
            http_only=True,
            same_site=None,
        ):

        cookie_value = f'{key}={value}'

        if max_age is not None:
            cookie_value += f'; Max-Age={max_age}'

        if expires is not None:
            cookie_value += f'; Expires={expires}'

        if domain is not None:
            cookie_value += f'; Domain={domain}'

        if path is not None:
            cookie_value += f'; Path={path}'

        if same_site is not None:
            cookie_value += f'; SameSite={same_site}'

        if secure is True:
            cookie_value += f'; Secure'

        if http_only is True:
            cookie_value += f'; HttpOnly'

        self._headers.append([
            'Set-Cookie'.encode('utf-8', 'strict'),
            cookie_value.encode('utf-8', 'strict')
        ])

    def get_body(self):
        return str.encode(self.content, self.encoding)

    def get_default_headers(self):
        return self.default_headers


class RedirectResponse(Response):

    def __init__(self, url, permanent=False):
        self._url = url
        self._permanent = permanent
        self._status = 302

        if self._permanent is True:
            self._status = 301

        headers = {
            'Location': self._url
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
        template_engine = settings.TEMPLATE_ENGINE
        context = self.context
        context['request'] = self.request
        return template_engine.render(self.template, context)


class NotFoundResponse(Response):

    def __init__(self, content='Not found'):
        super().__init__(None, content, status=404)


class NotImplementedResponse(Response):

    def __init__(self, content='Method not implemented'):
        super().__init__(None, content, status=501)


class RouteNotFoundResponse(Response):

    def __init__(self, content='Route not found'):
        super().__init__(None, content, status=404)


class ServerErrorResponse(Response):

    def __init__(self, content='Server error'):
        super().__init__(None, content, status=500)
