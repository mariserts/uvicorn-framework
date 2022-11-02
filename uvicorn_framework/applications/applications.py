from ..conf import settings
from ..http.responses import NotImplementedResponse


class Application:

    def __init__(self, settings=settings):
        self.settings = settings
        self.set_routes()

    async def __call__(self, scope, receive, send):
        message = await receive()
        print('(%s) message from  recv is %r' % (id(self),message))
        if message['type'] == 'lifespan.startup':
            await send({'type': 'lifespan.startup.complete'})
        elif message['type'] == 'lifespan.shutdown':
            await send({'type': 'lifespan.shutdown.complete'})
            return

        if message["type"] == "http.disconnect":
            return
        else:
            if not message.get("more_body"):
                body = message.get('body', b'')
                response = self.response(scope, body, send)
                await send(response.start)
                await send(response.body)

    def response(self, scope, receive, send):
        return NotImplementedResponse()

    def set_routes(self):
        for route in self.settings.ROUTES:
            self.settings.ROUTER.register(route)


class HttpApplication(Application):

    def response(self, scope, receive, send):
        request = self.settings.REQUEST_CLASS(scope, receive, self.settings)
        assert request.type == 'http'
        return self.settings.ROUTER.get_reponse(request, self.settings)
