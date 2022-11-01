from uvicorn_framework.http.responses import RedirectResponse,TemplateResponse
from uvicorn_framework.viewsets import ViewSet


class ProjectViewSet(ViewSet):

    template = 'uvicorn_framework_cms/admin/base.html'

    def get(self, request, id):
        return TemplateResponse(
            request,
            self.template,
            context=self.get_context()
        )

    def post(self, request, id):
        # Update, remove project
        return RedirectResponse('/')

    def get_context(self):
        return {}
