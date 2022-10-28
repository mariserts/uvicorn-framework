from uvicorn_framework.conf import Settings as UvicornFrameworkSettings

from uvicorn_framework_cms.conf import ROUTES as UFC_ROUTES


class Settings(UvicornFrameworkSettings):

    APPS = [
        'uvicorn_framework_cms',
    ]

    ROUTES = []
    ROUTES += UFC_ROUTES


settings = Settings()
