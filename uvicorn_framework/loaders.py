from importlib import import_module


def module_class_loader(string):

    if isinstance(string, str) is False:
        raise TypeError('"string" must be instance of str')

    parts = string.split('.')

    cls = parts.pop()
    module = import_module('.'.join(parts))

    return getattr(module, cls)
