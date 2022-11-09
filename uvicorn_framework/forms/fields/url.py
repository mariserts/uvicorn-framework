from urllib.parse import urlparse

from ..exceptions import get_field_is_message, FieldValidationError

from .base import BaseField


class URLField(BaseField):

    field_type = 'url'

    def is_valid(self):

        not_url_msg = get_field_is_message(self.name, 'is not a valid URL')

        self.check_required()

        if self.value is not None:

            try:
                result = urlparse(self.value)
            except ValueError:
                raise FieldValidationError(
                    field=self.name,
                    message=not_url_msg
                )

            if all([result.scheme, result.netloc]) is False:
                raise FieldValidationError(
                    field=self.name,
                    message=not_url_msg
                )

        return True
