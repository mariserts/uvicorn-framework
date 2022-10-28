import re


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


def route(pattern, view, name):
    return Route(pattern, view, name)
