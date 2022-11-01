import os

from .applications import HttpApplication
from .database.engines.sqlite import SqliteDatabaseEngine
from .database.models import Model
from .http.requests import Request
from .routers import Router, route
from .template_engines.template_engines import TemplateEngine


class Settings:

    __DB_ENGINE = None
    __DB_SESSION = None
    __ROUTER = None
    __TEMPLATE_ENGINE = None

    APPLICATION_CLASS = HttpApplication
    APPS = []

    DB_ENABLED = True
    DB_ENGINE_CLASS = SqliteDatabaseEngine
    DB_URL = 'sqlite:///db.sqlite3'

    DEBUG = True

    DIR =  os.path.dirname(os.path.abspath(__file__))

    REQUEST_CLASS = Request

    ROUTER_CLASS = Router

    ROUTES = []

    SECRET_KEY = 'test'

    TEMPLATE_ENGINE_CLASS = TemplateEngine
    TEMPLATE_ENCODING = 'utf-8'
    TEMPLATES_DIR = 'templates'

    @property
    def DB_ENGINE(self):
        if self.__DB_ENGINE is not None:
            return self.__DB_ENGINE
        self.__DB_ENGINE = self.DB_ENGINE_CLASS(self)
        return self.__DB_ENGINE

    def DB_MIGRATE(self):
        Model.metadata.create_all(self.DB_ENGINE.engine)

    @property
    def ROUTER(self):
        if self.__ROUTER is not None:
            return self.__ROUTER
        self.__ROUTER = self.ROUTER_CLASS()
        return self.__ROUTER

    @property
    def TEMPLATE_ENGINE(self):
        if self.__TEMPLATE_ENGINE is not None:
            return self.__TEMPLATE_ENGINE
        self.__TEMPLATE_ENGINE = self.TEMPLATE_ENGINE_CLASS(self)
        return self.__TEMPLATE_ENGINE


settings = Settings()
