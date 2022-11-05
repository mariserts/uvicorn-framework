from uvicorn_framework.http.responses import Response
from uvicorn_framework.viewsets import ViewSet



class HomeViewSet(ViewSet):

    def get(self, request):
        return Response(request, 'x/base.html')
