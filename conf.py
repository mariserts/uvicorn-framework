import os

from uvicorn_framework.conf import Settings as UvicornFrameworkSettings

from uvicorn_framework_cms.conf import settings as UFCSettings
from uvicorn_framework_cms.database.models import User


class Settings(UvicornFrameworkSettings):

    APPS = [
        'uvicorn_framework_cms',
    ]

    DIR = os.path.dirname(os.path.abspath(__file__))

    ROUTES = []

    def DB_MIGRATE(self):
        super().DB_MIGRATE()
        UFCSettings.DB_MIGRATE(self.DB_ENGINE)


settings = Settings()


UFCSettings.extend(settings)
