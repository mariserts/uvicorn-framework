from uvicorn_framework.conf import Settings as UvicornFrameworkSettings
from uvicorn_framework.routers import Router, route

from test_app.views import HomeViewSet, SlugViewSet, RedirectViewSet


router = Router()
router.register(r'/do/redirect/', RedirectViewSet, 'redirect')
router.register(r'/(?P<slug>[a-z]+)/', SlugViewSet, 'slug')
router.register(r'/', HomeViewSet, 'home')


class Settings(UvicornFrameworkSettings):

    APPS = [
        'test_app',
    ]
    ROUTER = router


settings = Settings()
