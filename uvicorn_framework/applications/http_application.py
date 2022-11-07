from ..conf import settings
from ..loaders import import_string

from .base import BaseApplication


app_name = settings.APP_NAME

router = f'{app_name}.routers.routers.Router'
request = f'{app_name}.http.requests.Request'
template_engine = f'{app_name}.template_engines.jinja2.Jinja2TemplateEngine'
db_engine = f'{app_name}.database.engines.sqlite.SqliteDatabaseEngine'
db_model_class = f'{app_name}.database.models.Model'


class HttpApplication(BaseApplication):

    def __init__(self,
            router_class=router,
            request_class=request,
            template_engine=template_engine,
            db_engine=db_engine,
            db_model_class=db_model_class,
            extra_settings=None
        ):

        self.db_engine = import_string(db_engine)
        self.db_model_class = import_string(db_model_class)
        self.template_engine = import_string(template_engine)

        super().__init__(
            router_class=router_class,
            request_class=request_class,
            extra_settings=extra_settings
        )

    def response(self, scope, receive, send):
        request = settings.REQUEST_CLASS(scope, receive)
        assert request.type == 'http'
        return settings.ROUTER.get_reponse(request)

    def extend_settings(self, settings_to_extend):
        settings_to_extend.DB_ENGINE_CLASS = self.db_engine
        settings_to_extend.DB_MODEL_CLASS = self.db_model_class
        settings_to_extend.REQUEST_CLASS = self.request_class
        settings_to_extend.ROUTER_CLASS = self.router_class
        settings_to_extend.TEMPLATE_ENGINE_CLASS = self.template_engine
        self.extra_settings.extend(settings_to_extend)
