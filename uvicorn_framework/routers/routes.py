from .base import BaseRoute


class Route(BaseRoute):

    def get_pattern_as_string(self):
        return self.pattern.pattern

    def reverse(self, kwargs={}):

        pattern = self.get_pattern_as_string()
        url = str(pattern)

        for key, value in kwargs.items():
            url = re.sub(rf'\(\?P\<{key}\>[^\)]+\)', str(value), url)

        return url


# --

def route(pattern, view, name):
    return Route(pattern, view, name)
