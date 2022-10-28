from .base import ContentType


class ContentTypeRegistry:

    content_type = ContentType
    content_types = {}

    def __init__(self):
        pass

    def register(self, content_type):
        if isinstance(content_type, self.content_type) is False:
            raise Exception(f'Must be of type {self.content_type.__name__}')
        self.content_types[content_type.name] = content_type

    def get_content_type(self, name):
        return self.content_types[name]
