def module_class_loader(string):

    parts = string.split('.')

    module = __import__(parts[0])

    for part in parts[1:]:
        module = getattr(module, part)

    return module
