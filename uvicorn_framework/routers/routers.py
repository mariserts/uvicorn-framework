import re

from uvicorn_cms.core.responses import (
    NotFoundResponse,
    NotImplementedResponse,
    ServerErrorResponse
)


class Route:

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

    def get_pattern_as_string(self):
        return self.pattern.pattern


class Router:

    routes = {}

    def __init__(self):
        pass

    def register(self, pattern, view, name):
        route = Route(pattern, view, name)
        self.routes[route.get_pattern_as_string()] = route

    def get_route_for_path(self, path):

        for key, item in self.routes.items():

            match = re.fullmatch(item.pattern, path)
            if match is not None:
                kwargs_match = re.search(item.pattern, path)
                return {
                    'view': item.view,
                    'kwargs': match.groupdict(),
                }

        return None

    def get_reponse(self, request, settings):

        response = NotFoundResponse()

        route = self.get_route_for_path(request.path)

        if route is None:
            return response

        view = route['view']
        kwargs = route['kwargs']

        if request.method not in view.HTTP_METHODS:
            return NotImplementedResponse()

        view_method = hasattr(view, request.method)

        if view_method is False:
            return NotImplementedResponse()

        if getattr(settings, 'DEBUG', True) is True:
            response = getattr(view(), request.method)(request, **kwargs)

        else:
            try:
                response = getattr(view, request.method)(request, **kwargs)
            except Exception as e:
                return ServerErrorResponse()

        return response


def route(pattern, view, name):
    return Route(pattern, view, name)
