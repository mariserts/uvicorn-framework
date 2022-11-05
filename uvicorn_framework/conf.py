import os


class BaseSettings:

    def __init__(self):
        pass

    def extend(self, external_settings_object):
        raise NotImplemented()


class Settings(BaseSettings):

    APP_NAME = 'uvicorn_framework'

    # __DB_ENGINE = None
    __ROUTER = None
    __TEMPLATE_ENGINE = None

    APPS = []

    DB_ECHO = False
    DB_ENABLED = True
    DB_ENGINE_CLASS = None
    DB_MODEL_CLASS = None
    DB_URL = 'sqlite:///db.sqlite3'

    DEBUG = False

    DIR = os.path.dirname(os.path.abspath(__file__))

    ENCODING = 'utf-8'

    REQUEST_CLASS = None

    ROUTER_CLASS = None

    ROUTES = []

    SECRET_KEY = '5ampl3-k3y'

    TEMPLATE_ENGINE_CLASS = None
    TEMPLATE_ENCODING = 'utf-8'
    TEMPLATES_DIR = 'templates'

    @property
    def DB_ENGINE(self):
        if self.__DB_ENGINE is not None:
            return self.__DB_ENGINE
        self.__DB_ENGINE = self.DB_ENGINE_CLASS()
        return self.__DB_ENGINE

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
        self.__TEMPLATE_ENGINE = self.TEMPLATE_ENGINE_CLASS()
        return self.__TEMPLATE_ENGINE

    def extend_self_from_object(self, external_settings_object):
        external_settings_object.extend(self)


settings = Settings()
