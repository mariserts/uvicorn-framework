def password_is_valid(
        password,
        min_chars=8,
        request_special_chars=True,
        request_digits=True
    ):

    special_characters = [
        '!',
        '@',
        '#',
        '$',
        '%',
        '&',
        '(',
        ')',
    ]

    digits = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        0,
    ]

    if len(password) < min_chars:
        return False

    if request_special_chars is True:
        if special_characters not in password:
            return False

    if request_digits is True:
        if digits not in password:
            return False

    return True
