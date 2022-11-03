from uvicorn_framework.conf import settings
from uvicorn_framework.http.responses import RedirectResponse

from ..http.resolvers import reverse
from ..http.responses import PermissionDeniedResponse


def authentication_required(func):

    def wrapper_func(view, request, *args, **kwargs):

        user = request.get_request_user()
        if user is None:
            redirect_to = reverse(settings.CMS_SIGN_IN_URLNAME)
            redirect_to += '?redirect_to=' + request.path
            return RedirectResponse(redirect_to)

        return func(view, request, *args, **kwargs)

    return wrapper_func
