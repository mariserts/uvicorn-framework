import os

from uvicorn_framework.conf import BaseSettings
from uvicorn_framework.routers.routes import route

from .viewsets import HomeViewSet


class Settings(BaseSettings):

    APPS = [
        'demo_app'
    ]

    DIR = os.path.dirname(os.path.abspath(__file__))

    ROUTES = [
        route(r'/', HomeViewSet, 'home')
    ]

    def extend(self, settings_to_extend):
        settings_to_extend.DIR = self.DIR
        settings_to_extend.APPS = settings_to_extend.APPS + self.APPS
        settings_to_extend.ROUTES = self.ROUTES


settings = Settings()
