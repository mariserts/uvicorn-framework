from uvicorn_framework.conf import settings
from uvicorn_framework.http.responses import RedirectResponse
from uvicorn_framework.viewsets import ViewSet

from ...database.lookups.authenticate import sign_out


class SignOutViewSet(ViewSet):

    def get(self, request):

        sign_out(request.session_token, request.user.id)

        response = RedirectResponse('/')

        response.set_cookie(
            settings.SESSION_COOKIE_NAME,
            '-1',
            max_age=-9999
        )

        return response
