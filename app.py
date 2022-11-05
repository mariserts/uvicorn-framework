from uvicorn_framework.applications.http_application import HttpApplication

from demo_app.conf import settings


app = HttpApplication(extra_settings=settings)
