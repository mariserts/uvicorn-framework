from .. import constants
from ..cryptography import hashed_value_matches
from ..http.responses import BadRequestResponse


def csrf_token_required(func):

    def wrapper_func(view, request, *args, **kwargs):

        hashed_csrf = None
        response_class = BadRequestResponse

        if request.method == 'post':

            try:
                hashed_csrf = request.body[constants.FIELD_NAME_CSRF_TOKEN]
            except KeyError:
                return response_class(content='Missing CSRF token')

            if hashed_value_matches(request.csrf_token, hashed_csrf) is False:
                return response_class(content='CSRF token is incorrect')

        return func(view, request, *args, **kwargs)

    return wrapper_func
