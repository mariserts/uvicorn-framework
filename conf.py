from uvicorn_framework.conf import Settings as UvicornFrameworkSettings
from uvicorn_framework.routers import route

from test_app.views import HomeViewSet, SlugViewSet, RedirectViewSet


class Settings(UvicornFrameworkSettings):

    APPS = [
        'test_app',
    ]

    ROUTES = [
        route(r'/do/redirect/', RedirectViewSet, 'redirect'),
        route(r'/(?P<slug>[a-z]+)/', SlugViewSet, 'slug'),
        route(r'/', HomeViewSet, 'home')
    ]


settings = Settings()
