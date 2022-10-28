from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .applications import HttpApplication
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

    DEBUG = True

    DB_ENABLED = True
    DB_URL = 'sqlite://'

    REQUEST_CLASS = Request

    ROUTER_CLASS = Router

    ROUTES = []

    SECRET_KEY = 'test'

    TEMPLATES_DIR = 'templates'
    TEMPLATE_ENCODING = 'utf-8'

    @property
    def DB_ENGINE(self):
        if self.__DB_ENGINE is not None:
            return self.__DB_ENGINE
        self.__DB_ENGINE = create_engine(self.DB_URL, echo=True)
        return self.__DB_ENGINE

    @property
    def DB_CURSOR(self):
        if self.__DB_SESSION is not None:
            return self.__DB_SESSION
        self.__DB_SESSION = sessionmaker(bind=self.DB_ENGINE)
        return self.__DB_SESSION

    def DB_MIGRATE(self):
        Model.metadata.create_all(self.DB_ENGINE)

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
        self.__TEMPLATE_ENGINE = TemplateEngine(self)
        return self.__TEMPLATE_ENGINE


settings = Settings()
