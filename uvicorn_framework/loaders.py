from importlib import import_module


def import_string(string):

    if isinstance(string, str) is False:
        raise TypeError('"string" must be instance of str')

    parts = string.split('.')

    cls = parts.pop()
    module = import_module('.'.join(parts))

    return getattr(module, cls)
