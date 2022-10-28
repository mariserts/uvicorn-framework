import bcrypt


def hash_value(value, salt='-', encoding='utf-8'):
    value_bytes = value.encode(encoding, 'strict')
    salt_bytes = salt.encode(encoding, 'strict')
    hashed_value = bcrypt.hashpw(value_bytes, salt_bytes)
    return hashed_value.decode(encoding, 'strict')
