from uvicorn_framework.applications.http_application import HttpApplication

from conf import settings


app = HttpApplication(extra_settings=settings)
