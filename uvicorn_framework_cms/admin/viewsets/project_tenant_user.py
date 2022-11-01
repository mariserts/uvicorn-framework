from uvicorn_framework.http.responses import RedirectResponse,TemplateResponse
from uvicorn_framework.viewsets import ViewSet


class ProjectTenantUserViewSet(ViewSet):

    template = 'uvicorn_framework_cms/admin/base.html'

    def get(self, request, project_id, tenant_id, id):
        return TemplateResponse(
            request,
            self.template,
            context=self.get_context()
        )

    def post(self, request, project_id, tenant_id, id):
        # Updates ACL
        # Removes user
        return RedirectResponse('/')

    def get_context(self):
        return {}
