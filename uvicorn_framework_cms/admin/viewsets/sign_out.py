from uvicorn_framework.conf import settings
from uvicorn_framework.http.responses import RedirectResponse
from uvicorn_framework.viewsets import ViewSet

from ... import constants
from ...database.queries.authenticate import sign_out
from ...http.resolvers import reverse


class SignOutViewSet(ViewSet):

    def get(self, request):

        redirect_to = reverse(constants.URLNAME_CMS_SIGN_IN)

        if request.user is not None:
            sign_out(request.session_token, request.user.id)

        response = RedirectResponse(redirect_to)

        response.set_cookie(
            settings.SESSION_COOKIE_NAME,
            '-1',
            max_age=-9999
        )

        return response
