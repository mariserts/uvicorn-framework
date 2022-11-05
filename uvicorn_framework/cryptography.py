import hashlib

from .conf import settings


def hash_value(
        password: str,
        algorithm: str = 'sha256',
        encoding: str = settings.ENCODING,
        salt: str =settings.SECRET_KEY
    ) -> str:

    _salt = str(salt).encode(encoding, 'strict')
    _password = password.encode(encoding, 'strict')

    hasher = hashlib.new(algorithm)

    hasher.update(_salt)
    hasher.update(_password)

    return hasher.hexdigest()


def hashed_value_matches(
        password: str,
        hashed_password: str
    ) -> bool:
    return hash_value(password) == hashed_password
