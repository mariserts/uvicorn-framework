import unittest

from ...forms.exceptions import FieldValidationError
from ...forms.fields.url import URLField


class URLFieldTestCase(unittest.TestCase):

    def setUp(self):
        self.exception = FieldValidationError
        self.field = URLField

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
            value='/xyz/base.html'
        )

        with self.assertRaises(FieldValidationError):
            field.is_valid()

        field3 = self.field(
            required=False,
            value='http://example.com'
        )

        self.assertIs(field3.is_valid(), True)

        field4 = self.field(
            required=False,
            value='http://example.com/example/?example=example'
        )

        self.assertIs(field4.is_valid(), True)

        field5 = self.field(
            required=False,
            value='ftp://127.0.0.1:8000/'
        )

        self.assertIs(field5.is_valid(), True)
