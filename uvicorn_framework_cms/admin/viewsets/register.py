from uvicorn_framework.conf import settings

from uvicorn_framework.http.responses import RedirectResponse, Response, TemplateResponse
from uvicorn_framework.viewsets import ViewSet

from ...database.lookups.authenticate import register
from ...database.lookups.users import get_user
from ...validators.emails import email_is_valid


class RegisterViewSet(ViewSet):

    template = 'uvicorn_framework_cms/admin/pages/register.html'

    def get(self, request):

        context = self.get_context()
        context['request'] = request

        return TemplateResponse(
            request,
            self.template,
            context=context
        )

    def post(self, request):

        email = request.body['email']
        password = request.body['password']
        password2 = request.body['password2']

        if password != password2:
            raise Exception('Passowrds do not match')

        if email_is_valid(email) is False:
            raise Exception('Email is invalid')

        user = get_user(email=email)
        if user is not None:
            raise Exception('Email is in use')

        user = register(email, password)

        return RedirectResponse('/cms/')

    def get_context(self):
        return {}
