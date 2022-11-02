import hashlib


def hash_password(password, algorithm='sha256', encoding='utf-8'):
    hasher = hashlib.new(algorithm)
    hasher.update(password.encode(encoding, 'strict'))
    return hasher.hexdigest()


def password_matches(password, hashed_password):
    return hash_password(password) == hashed_password
