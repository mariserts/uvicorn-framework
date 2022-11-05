from jinja2 import Environment, FileSystemLoader, select_autoescape

from ..conf import settings

from .base import BaseTemplateEngine


class Jinja2TemplateEngine(BaseTemplateEngine):

    _env = None

    @property
    def encoding(self):
        return settings.TEMPLATE_ENCODING

    @property
    def environment(self):

        if self._env is not None:
            return self._env

        paths = []

        for app in settings.APPS:
            paths.append(f'{app}/{settings.TEMPLATES_DIR}')

        self._env = Environment(
            loader=FileSystemLoader(
                paths,
                encoding=self.encoding
            ),
            autoescape=select_autoescape()
        )

        return self._env

    @property
    def package_path(self):
        return self.settings.TEMPLATES_DIR

    def get_template(self, template):
        return self.environment.get_template(template)

    def render(self, template, context={}):
        template = self.get_template(template)
        return template.render(**context)
