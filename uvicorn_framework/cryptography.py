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
        value: str,
        hashed_value: str
    ) -> bool:
    return hash_value(value) == hashed_value
