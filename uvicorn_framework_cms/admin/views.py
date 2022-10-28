from uvicorn_framework.http.responses import RedirectResponse, TemplateResponse
from uvicorn_framework.views.viewsets import ViewSet


class LogInViewSet(ViewSet):

    def get(self, request):
        return TemplateResponse(request, self.template, self.get_context())

    def post(self, request):
        return RedirectResponse('/')

    def get_context(self):
        return {}
