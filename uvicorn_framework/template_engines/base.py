from ..conf import settings


class BaseTemplateEngine:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def get_template(self, template):
        raise NotImplemented()

    def render(self, template, context={}):
        raise NotImplemented()
