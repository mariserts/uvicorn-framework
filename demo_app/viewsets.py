from uvicorn_framework.http.responses import RedirectResponse, TemplateResponse
from uvicorn_framework.viewsets import ViewSet


class TemplateViewSet(ViewSet):

    def get(self, request):
        return TemplateResponse(request, 'demo_app/base.html')


class RedirectViewSet(ViewSet):

    def get(self, request):
        return RedirectResponse('/')
