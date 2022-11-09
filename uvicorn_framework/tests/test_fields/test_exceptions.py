import unittest

from ...forms.exceptions import (
    get_field_require_type_message,
    get_field_is_required_message,
    get_field_is_message,
)


class ExceptionTextGeneratorTestCase(unittest.TestCase):

    def test_get_field_is_required_message(self):

        name = 'XXX'

        self.assertEquals(
            get_field_is_required_message(name),
            f'Field "{name}" is required'
        )

    def test_get_field_require_type_message(self):

        name = 'XXX'
        field_type = 'number'

        self.assertEquals(
            get_field_require_type_message(name, field_type),
            f'Field "{name}" must be {field_type}'
        )

    def test_get_field_is_message(self):

        name = 'XXX'
        text = 'is XXX'

        self.assertEquals(
            get_field_is_message(name, text),
            f'Field "{name}" {text}'
        )
