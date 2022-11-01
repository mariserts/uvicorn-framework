from uvicorn_framework.http.responses import RedirectResponse,TemplateResponse
from uvicorn_framework.viewsets import ViewSet


class TenantViewSet(ViewSet):

    template = 'uvicorn_framework_cms/admin/base.html'

    def get(self, request, id):
        # Requires superuser or tenant user
        return TemplateResponse(
            request,
            self.template,
            context=self.get_context()
        )

    def post(self, request, id):
        # Requires superuser or tenant user
        # Updates tenant
        # Superuser can remove tenant
        return RedirectResponse('/')

    def get_context(self):
        return {}
