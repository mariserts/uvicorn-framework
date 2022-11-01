import re

from ..http.responses import (
    NotFoundResponse,
    NotImplementedResponse,
    RouteNotFoundResponse,
    ServerErrorResponse
)


class Router:

    __unset_cache_value = '-1'
    __cache_paths = {}
    routes = []

    def __init__(self):
        pass

    def get_cached_route(self, path):
        return self.__cache_paths.get(path, self.__unset_cache_value)

    def set_cached_route(self, path, data):
        self.__cache_paths[path] = data

    def register(self, route):
        self.routes.append(route)

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

    def get_reponse(self, request, settings):

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
            response = getattr(view(), request.method)(request, **kwargs)

        else:
            try:
                response = getattr(view, request.method)(request, **kwargs)
            except Exception as e:
                return ServerErrorResponse()

        return response
