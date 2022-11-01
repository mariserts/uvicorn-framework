from uvicorn_framework.http.responses import RedirectResponse, Response, TemplateResponse
from uvicorn_framework.viewsets import ViewSet


class SignInViewSet(ViewSet):

    template = 'uvicorn_framework_cms/admin/base.html'

    def get(self, request):

        response = TemplateResponse(
            request,
            self.template,
            context=self.get_context(),
        )

        response.set_cookie('1', 1)
        response.set_cookie('2', 2)

        return response

    def post(self, request):
        return RedirectResponse('/')

    def get_context(self):
        return {}
