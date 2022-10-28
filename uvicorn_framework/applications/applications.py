from ..conf import settings as UvicornFrameworkSettings

from ..http.responses import NotImplementedResponse


class Application:

    def __init__(
        self,
        scope,
        receive,
        send,
        settings=UvicornFrameworkSettings
    ):
        self.scope = scope
        self.receive = receive
        self.send = send
        self.settings = settings

    @property
    def response(self):
        return NotImplementedResponse()


class HttpApplication(Application):

    @property
    def response(self):
        request = self.settings.REQUEST(self.scope, self.settings)
        assert request.type == 'http'
        return self.settings.ROUTER.get_reponse(request, self.settings)
