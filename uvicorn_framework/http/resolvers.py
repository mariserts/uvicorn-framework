from uvicorn_framework.conf import settings


def reverse(name, kwargs={}):
    return settings.ROUTER.reverse(name, kwargs)
