from uvicorn_framework.http.responses import RedirectResponse,TemplateResponse
from uvicorn_framework.viewsets import ViewSet


class ProjectsViewSet(ViewSet):

    template = 'uvicorn_framework_cms/admin/pages/projects.html'

    def get(self, request):
        return TemplateResponse(
            request,
            self.template,
            context=self.get_context()
        )

    def post(self, request):
        # Add new project
        return RedirectResponse('/')
