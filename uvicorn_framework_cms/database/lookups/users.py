from ..models import User


def hash_password(password):
    return password


def password_matches(password, hashed_password):
    return hash_password(password) == hashed_password


def create_user(
        cursor,
        email,
        password,
        is_superuser=False
    ):

    user = User(
        email=email,
        password=hash_password(password),
        is_superuser=is_superuser
    )

    cursor.add(user)
    cursor.commit()

    return user


def update_user(
        cursor,
        id,
        password=None,
        is_superuser=False
    ):

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
        cursor,
        id=None,
        email=None,
        is_superuser=None
    ):

    condition_kwargs = {}

    if id is not None:
        condition_kwargs['id'] = id

    if email is not None:
        condition_kwargs['email'] = email

    if is_superuser is not None:
        condition_kwargs['is_superuser'] = is_superuser

    user = cursor.query(User).filter_by(**condition_kwargs).first()

    return user
