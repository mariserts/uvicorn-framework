import re

from ..conf import settings
from ..http.responses import (
    NotFoundResponse,
    NotImplementedResponse,
    RouteNotFoundResponse,
    ServerErrorResponse
)

from .base import BaseRouter


class Router(BaseRouter):

    __unset_cache_value = '-1'
    __cache_paths = {}

    def __init__(self):
        pass

    def get_cached_route(self, path):
        return self.__cache_paths.get(path, self.__unset_cache_value)

    def set_cached_route(self, path, data):
        self.__cache_paths[path] = data

    def reverse(self, name, kwargs):
        for route in self.routes:
            if route.name == name:
                return route.reverse(kwargs)
        raise Exception(f'Route not found for name "{name}"')

    def get_route_for_path(self, path):

        if path.endswith('/') is False:
            path += '/'

        cached_data = self.get_cached_route(path)
        if cached_data is None:
            return cached_data

        if cached_data == self.__unset_cache_value:

            cached_data = None

            for route in self.routes:

                match = re.fullmatch(route.pattern, path)
                if match is not None:
                    kwargs_match = re.search(route.pattern, path)
                    cached_data = {
                        'route': route,
                        'kwargs': match.groupdict(),
                    }
                    break

            self.set_cached_route(path, cached_data)

        return cached_data

    def get_reponse(self, request):

        data = self.get_route_for_path(request.path)

        if data is None:
            return RouteNotFoundResponse()

        route = data['route']
        kwargs = data['kwargs']

        view = route.view

        if request.method not in view.HTTP_METHODS:
            return NotImplementedResponse()

        view_method = hasattr(view, request.method)

        if view_method is False:
            return NotImplementedResponse()

        if getattr(settings, 'DEBUG', True) is True:
            response = getattr(
                view(request), request.method)(request, **kwargs)

        else:
            try:
                response = getattr(
                    view(request), request.method)(request, **kwargs)
            except Exception as e:
                return ServerErrorResponse(str(e))

        return response
