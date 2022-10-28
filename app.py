from uvicorn_framework.applications import HttpApplication

from conf import settings


async def app(scope, receive, send):
    application = HttpApplication(scope, receive, send, settings)
    await send(application.response.start)
    await send(application.response.body)
