from uvicorn_framework.http.responses import RedirectResponse, Response, TemplateResponse
from uvicorn_framework.viewsets import ViewSet


class HomeViewSet(ViewSet):

    def get(self, request):
        return Response(request, 'This is home')


class SlugViewSet(ViewSet):

    def get(self, request, slug):
        return TemplateResponse(
            request,
            'base.html',
            context={'slug': slug}
        )


class RedirectViewSet(ViewSet):

    def get(self, request):
        return RedirectResponse('/')
