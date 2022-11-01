class BaseContentType:
    name = ''


class BaseContentTypeRegistry:

    content_type_class = BaseContentType
    content_types = {}

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def register(self, content_type):
        if isinstance(content_type, self.content_type_class) is False:
            raise Exception(
                f'Must be of type {self.content_type_class.__name__}')
        self.content_types[content_type.name] = content_type

    def get_content_type(self, name):
        return self.content_types[name]
