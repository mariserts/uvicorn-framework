from uvicorn_app.http.responses import Response, TemplateResponse
from uvicorn_app.viewsets.viewsets import ViewSet


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
