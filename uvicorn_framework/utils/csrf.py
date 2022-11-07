import uuid

from ..cryptography import hash_value


def create_csrf_token(request):
    return hash_value(request.id)


def create_form_csrf_token(request):
    return hash_value(request.csrf_token)
