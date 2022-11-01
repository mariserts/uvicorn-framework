from uvicorn_framework.http.responses import RedirectResponse,TemplateResponse
from uvicorn_framework.viewsets import ViewSet


class TenantsViewSet(ViewSet):

    template = 'uvicorn_framework_cms/admin/base.html'

    def get(self, request):
        # Requires superuser or tenant admin
        return TemplateResponse(
            request,
            self.template,
            context=self.get_context()
        )

    def post(self, request):
        # Requires superuser
        # Superuser can add new tenant
        return RedirectResponse('/')

    def get_context(self):
        return {}
