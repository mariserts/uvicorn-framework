from ..exceptions import FieldValidationError

from .base import BaseField


class TextField(BaseField):

    field_type = 'text'

    def __repr__(self):
        return str(self.value)
