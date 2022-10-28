from jinja2 import Environment, FileSystemLoader, select_autoescape


class TemplateEngine:

    _env = None

    def __init__(self, settings):
        self._settings = settings

    @property
    def encoding(self):
        return self.settings.TEMPLATE_ENCODING

    @property
    def environment(self):

        if self._env is not None:
            return self._env

        paths = []
        for app in self.settings.APPS:
            paths.append(f'{app}/{self.package_path}')

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

    @property
    def settings(self):
        return self._settings

    def get_template(self, template):
        return self.environment.get_template(template)

    def render(self, template, context={}):
        template = self.get_template(template)
        return template.render(**context)
