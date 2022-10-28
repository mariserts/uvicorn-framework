from ..http.responses import NotImplementedResponse


class Application:

    def __init__(self, settings):
        self.settings = settings
        self.set_routes()

    async def __call__(self, scope, receive, send):
        response = self.response(scope, receive, send)
        await send(response.start)
        await send(response.body)

    def response(self, scope, receive, send):
        return NotImplementedResponse()

    def set_routes(self):
        for route in self.settings.ROUTES:
            self.settings.ROUTER.register(route)


class HttpApplication(Application):

    def response(self, scope, receive, send):
        request = self.settings.REQUEST(scope, self.settings)
        assert request.type == 'http'
        return self.settings.ROUTER.get_reponse(request, self.settings)
