from uvicorn_framework.conf import settings

from uvicorn_framework.http.responses import RedirectResponse, Response, TemplateResponse
from uvicorn_framework.viewsets import ViewSet

from ... import constants
from ...database.lookups.authenticate import sign_in
from ...http.resolvers import reverse


class SignInViewSet(ViewSet):

    template = 'uvicorn_framework_cms/admin/pages/sign_in.html'

    def get(self, request):

        print(reverse(constants.URLNAME_CMS_SIGN_IN))

        context = self.get_context()
        context['request'] = request
        return TemplateResponse(request, self.template, context=context)

    def post(self, request):

        email = request.body['email']
        password = request.body['password']

        session = sign_in(
            email,
            password,
        )

        response = RedirectResponse('/cms/')

        if session is not None:
            response.set_cookie(
                settings.SESSION_COOKIE_NAME,
                session.id,
            )

        return response

    def get_context(self):
        return {}
