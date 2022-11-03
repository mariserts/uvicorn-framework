from uvicorn_framework.conf import settings

from ...cryptography import hash_password

from ..models import UserModel
from ..serializers.users import UserSerializer


def create_user(
        email,
        password,
        is_superuser=False
    ):

    user = None
    Session = settings.DB_ENGINE.session

    with Session() as cursor:

        user = UserModel(
            email=email,
            password=hash_password(password),
            is_superuser=is_superuser
        )

        cursor.add(user)
        cursor.commit()

        user = UserSerializer(
            id=user.id,
            email=user.email,
            password=user.password,
            is_superuser=user.is_superuser
        )

    return user


def update_user(
        id,
        password=None,
        is_superuser=False
    ):

    user = None
    Session = settings.DB_ENGINE.session

    with Session() as cursor:

        user = cursor.query(UserModel).filter_by(id=id).first()
        if user is None:
            raise Exception('User not found')

        update_kwargs = {}

        if password is not None:
            update_kwargs['password'] = hash_password(password)

        if id is not None:
            update_kwargs['is_superuser'] = is_superuser

        user.update(update_kwargs)

        cursor.commit()

        user = UserSerializer(
            id=user.id,
            email=user.email,
            password=user.password,
            is_superuser=user.is_superuser
        )

    return user


def get_user(
        id=None,
        email=None,
        is_superuser=None
    ):

    user = None
    Session = settings.DB_ENGINE.session

    with Session() as cursor:

        condition_kwargs = {}

        if id is not None:
            condition_kwargs['id'] = id

        if email is not None:
            condition_kwargs['email'] = email

        if is_superuser is not None:
            condition_kwargs['is_superuser'] = is_superuser

        user = cursor.query(UserModel).filter_by(**condition_kwargs).first()

        if user is None:
            return None

        user = UserSerializer(
            id=user.id,
            email=user.email,
            password=user.password,
            is_superuser=user.is_superuser
        )

    return user
