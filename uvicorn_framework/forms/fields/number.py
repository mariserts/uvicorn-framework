from .base import BaseField

from ..exceptions import (
    get_field_require_type_message,
    get_field_is_message,
    FieldValidationError
)


class NumberField(BaseField):

    field_type = 'number'

    def __init__(
            self,
            *args,
            **kwargs
        ):

        max = kwargs.pop('max', None)
        min = kwargs.pop('min', None)
        step = kwargs.pop('step', None)

        super().__init__(*args, **kwargs)

        self.max = max
        self.min = min
        self.step = step

    def is_valid(self):

        type_msg = get_field_require_type_message(self.name, 'number')
        too_big_msg = get_field_is_message(self.name, 'is too big')
        too_small_msg = get_field_is_message(self.name, 'is too small')

        self.check_required()

        if self.value is not None:

            if self.value.isdigit() is False:
                raise FieldValidationError(
                    field=self.name,
                    message=type_msg
                )

            value = int(self.value)

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

    def render_field(self):

        html = '<input '

        html += f'autocomplete="{self.autocomplete}" '

        if self.class_name is not None:
            html += f'class="{self.class_name}" '

        html += f'id="{self.id}" '

        if self.max is not None:
            html += f'max="{self.max}" '

        if self.min is not None:
            html += f'min="{self.min}" '

        html += f'name="{self.name}" '

        if self.placeholder is not None:
            html += f'placeholder="{self.placeholder}" '

        if self.required is True:
            html += f'required '

        if self.step is not None:
            html += f'step="{self.step}" '

        html += f'type="{self.field_type}" '

        html += f'value="{self.value}" '

        html += '/>'

        return html

    def __repr__(self):
        if self.value is None:
            return None
        return int(self.value)
