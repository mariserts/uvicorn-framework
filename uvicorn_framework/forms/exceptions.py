from ..exceptions import ValidationException


def get_field_is_message(name, text):
    return f'Field "{name}" {text}'


def get_field_is_required_message(name):
    return f'Field "{name}" is required'


def get_field_require_type_message(name, field_type):
    return f'Field "{name}" must be {field_type}'


class FieldValidationError(ValidationException):

    def __init__(self, field='', message=''):
        self.field = field
        self.message = message


class FormValidationError(ValidationException):

    def __init__(self, errors={}, message=''):
        self.errors = errors
        self.message = message
