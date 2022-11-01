from uvicorn_framework.http.responses import RedirectResponse,TemplateResponse
from uvicorn_framework.viewsets import ViewSet


class ProjectTenantItemViewSet(ViewSet):

    template = 'uvicorn_framework_cms/admin/base.html'

    def get(self, request, project_id, tenant_id, ct_name, id):
        return TemplateResponse(
            request,
            self.template,
            context=self.get_context()
        )

    def post(self, request, project_id, tenant_id, ct_name, id):
        return RedirectResponse('/')

    def get_context(self):
        return {}
