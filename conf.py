import os

from uvicorn_framework.conf import settings

from uvicorn_framework_cms.conf import Settings as UFCSettings


class Settings:

    APPS = [
        'uvicorn_framework_cms',
    ]

    DIR = os.path.dirname(os.path.abspath(__file__))

    ROUTES = []

    def DB_MIGRATE(self):
        super().DB_MIGRATE()
        UFCSettings.DB_MIGRATE(self.DB_ENGINE)

    def extend(self, base_settings):
        base_settings.APPS = self.APPS
        base_settings.DIR = self.DIR
        base_settings.ROUTES = self.ROUTES
        base_settings.DB_MIGRATE = self.DB_MIGRATE


Settings().extend(settings)
UFCSettings().extend(settings)
