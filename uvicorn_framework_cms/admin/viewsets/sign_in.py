from uvicorn_framework.conf import settings

from uvicorn_framework.http.responses import RedirectResponse, Response, TemplateResponse
from uvicorn_framework.viewsets import ViewSet

from ... import constants
from ...database.lookups.authenticate import sign_in
from ...http.resolvers import reverse


class SignInViewSet(ViewSet):

    template = 'uvicorn_framework_cms/admin/pages/sign_in.html'

    def get(self, request):
        return TemplateResponse(
            request,
            self.template,
            context=self.get_context()
        )

    def post(self, request):

        redirect_to = request.body.get('redirect_to', None)
        email = request.body['email']
        password = request.body['password']

        session = sign_in(
            email,
            password,
        )

        if redirect_to is None:
            redirect_to = reverse(constants.URLNAME_CMS_PROJECTS)

        response = RedirectResponse(redirect_to)

        if session is not None:
            response.set_cookie(
                settings.SESSION_COOKIE_NAME,
                session.id,
            )

        return response
