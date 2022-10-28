from uvicorn_framework.routers import route

from .admin.views import HomeViewSet, LogInViewSet


ROUTES = [
    route(r'/sign-in/', LogInViewSet, 'sign_in'),
    route(r'/', HomeViewSet, 'home'),
]
