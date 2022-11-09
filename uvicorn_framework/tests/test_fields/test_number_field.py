import unittest

from ...forms.exceptions import FieldValidationError
from ...forms.fields.number import NumberField


class NumberFieldTestCase(unittest.TestCase):

    def setUp(self):
        self.exception = FieldValidationError
        self.field = NumberField

    def test_required_attr(self):

        field = self.field(
            required=True,
        )

        with self.assertRaises(FieldValidationError):
            field.is_valid()


        field2 = self.field(
            required=False,
        )

        self.assertIs(field2.is_valid(), True)

    def test_value(self):

        field = self.field(
            required=False,
            value='a'
        )

        with self.assertRaises(FieldValidationError):
            field.is_valid()

        field2 = self.field(
            required=False,
            value='0.01'
        )

        with self.assertRaises(FieldValidationError):
            field.is_valid()

        field3 = self.field(
            required=False,
            value='1'
        )

        self.assertIs(field3.is_valid(), True)
