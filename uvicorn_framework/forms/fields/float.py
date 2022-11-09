from ..exceptions import (
    get_field_require_type_message,
    get_field_is_message,
    FieldValidationError
)

from .number import NumberField


class FloatField(NumberField):

    def is_valid(self):

        type_msg = get_field_require_type_message(self.name, 'float')
        too_big_msg = get_field_is_message(self.name, 'is too big')
        too_small_msg = get_field_is_message(self.name, 'is too small')

        self.check_required()

        if self.value is not None:

            try:
                value = float(self.value)
            except ValueError:
                raise FieldValidationError(
                    field=self.name,
                    message=type_msg
                )

            if self.min is not None:
                if value < self.min:
                    raise FieldValidationError(
                        field=self.name,
                        message=too_small_msg
                    )

            if self.max is not None:
                if value > self.max:
                    raise FieldValidationError(
                        field=self.name,
                        message=too_big_msg
                    )

        return True

    def __repr__(self):
        if self.value is None:
            return None
        return float(self.value)
