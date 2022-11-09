from .base import BaseField

from ...validators.emails import email_is_valid

from ..exceptions import get_field_is_message, FieldValidationError


class EmailField(BaseField):

    field_type = 'email'

    def is_valid(self):

        not_email_msg = get_field_is_message(
            self.name,
            'is not a valid email'
        )

        self.check_required()

        if self.value is not None:
            valid = email_is_valid(self.value)
            if valid is False:
                raise FieldValidationError(
                    field=self.name,
                    message=not_email_msg
                )

        return True
