from ...validators.passwords import password_is_valid

from ..exceptions import get_field_is_message, FieldValidationError

from .base import BaseField


class PasswordField(BaseField):

    field_type = 'password'

    def is_valid(self):

        not_password_msg = get_field_is_message(
            self.name,
            'is not valid password'
        )

        self.check_required()

        if self.value is not None:
            if password_is_valid(self.value) is False:
                raise FieldValidationError(
                    field=self.name,
                    message=not_password_msg
                )

        return True
