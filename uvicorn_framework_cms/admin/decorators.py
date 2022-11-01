from ..http.responses import PermissionDeniedResponse


def user_is_authenticated(func):

    def wrapper_func(view, request, *args, **kwargs):

        user = request.get_request_user()
        if user is None:
            return PermissionDeniedResponse()

        return func(view, request, *args, **kwargs)

    return wrapper_func


def user_is_superuser(func):

    def wrapper_func(view, request, *args, **kwargs):

        user = request.get_request_user()
        if user is None:
            return PermissionDeniedResponse()

        if user.is_superuser is False:
            return PermissionDeniedResponse()

        return func(view, request, *args, **kwargs)

    return wrapper_func
