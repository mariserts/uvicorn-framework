from ..conf import settings
from ..http.responses import NotImplementedResponse
from ..loaders import module_class_loader


class BaseApplication:

    def __init__(
            self,
            router_class,
            request_class,
            extra_settings
        ):
        self.router_class = module_class_loader(router_class)
        self.request_class = module_class_loader(request_class)
        self.extra_settings = extra_settings

        self.extend_settings(settings)
        self.set_routes()

    async def __call__(
            self,
            scope,
            receive,
            send
        ):

        if scope['type'] == 'lifespan':

            while True:
                message = await receive()
                if message['type'] == 'lifespan.startup':
                    await send({'type': 'lifespan.startup.complete'})
                elif message['type'] == 'lifespan.shutdown':
                    await send({'type': 'lifespan.shutdown.complete'})
                    return

        else:

            message = await receive()

            if message['type'] == 'lifespan.startup':
                await send({'type': 'lifespan.startup.complete'})
            elif message['type'] == 'lifespan.shutdown':
                await send({'type': 'lifespan.shutdown.complete'})
                return

            if message['type'] == 'http.disconnect':
                return
            else:
                if not message.get('more_body'):
                    body = message.get('body', b'')
                    response = self.response(scope, body, send)
                    await send(response.start)
                    await send(response.body)

    def response(self, scope, receive, send):
        return NotImplementedResponse()

    def set_routes(self):
        for route in settings.ROUTES:
            settings.ROUTER.register(route)

    def extend_settings(self, settings_to_extend):
        settings_to_extend.REQUEST_CLASS = self.request_class
        settings_to_extend.ROUTER_CLASS = self.router_class
        self.extra_settings.extend(settings_to_extend)
