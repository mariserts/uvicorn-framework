from uvicorn_framework.http.responses import RedirectResponse, TemplateResponse
from uvicorn_framework.viewsets import ViewSet

from ..decorators import authentication_required


class ProjectsViewSet(ViewSet):

    template = 'uvicorn_framework_cms/admin/pages/projects.html'

    @authentication_required
    def get(self, request):
        return TemplateResponse(
            request,
            self.template,
            context=self.get_context()
        )

    @authentication_required
    def post(self, request):
        # Add new project
        return RedirectResponse('/')

    def get_context(self):

        context = super().get_context()

        context['page'] = {
            'title': 'projects',
            'subsections': []
        }

        context['projects'] = {
            'results': [],
            'pages': 1,
            'page': 1,
            'total': 0,
        }

        return context
