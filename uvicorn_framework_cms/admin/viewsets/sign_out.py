from uvicorn_framework.http.responses import RedirectResponse
from uvicorn_framework.viewsets import ViewSet


class SignOutViewSet(ViewSet):

    def get(self, request):
        return RedirectResponse('/')
