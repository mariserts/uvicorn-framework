import re


class BaseRoute:

    def __init__(self, pattern, view, name):
        self._pattern = re.compile(pattern)
        self._view = view
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def pattern(self):
        return re.compile(self._pattern)

    @property
    def view(self):
        return self._view

    def reverse(self, kwargs={}):
        raise NotImplemented()


class BaseRouter:

    routes = []

    def __init__(self):
        pass

    def register(self, route):
        self.routes.append(route)

    def reverse(self, name, kwargs):
        raise NotImplemented()

    def get_route_for_path(self, path):
        raise NotImplemented()

    def get_reponse(self, request, settings):
        raise NotImplemented()
