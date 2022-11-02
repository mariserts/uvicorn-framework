from uvicorn_framework.conf import settings

from ...cryptography import hash_password

from ..models import User


def create_user(
        email,
        password,
        is_superuser=False
    ):

    cursor = settings.DB_ENGINE.cursor

    user = User(
        email=email,
        password=hash_password(password),
        is_superuser=is_superuser
    )

    cursor.add(user)
    cursor.commit()

    return user


def update_user(
        id,
        password=None,
        is_superuser=False
    ):

    cursor = settings.DB_ENGINE.cursor

    user = cursor.query(User).filter_by(id=id).first()

    if user is None:
        raise Exception('User not found')

    update_kwargs = {}

    if password is not None:
        update_kwargs['password'] = hash_password(password)

    if id is not None:
        update_kwargs['is_superuser'] = is_superuser

    user.update(update_kwargs)

    cursor.commit()

    return user


def get_user(
        id=None,
        email=None,
        is_superuser=None
    ):

    cursor = settings.DB_ENGINE.cursor

    condition_kwargs = {}

    if id is not None:
        condition_kwargs['id'] = id

    if email is not None:
        condition_kwargs['email'] = email

    if is_superuser is not None:
        condition_kwargs['is_superuser'] = is_superuser

    return cursor.query(User).filter_by(**condition_kwargs).first()
