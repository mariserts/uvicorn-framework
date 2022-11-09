import re

from ... import constants

from ..exceptions import get_field_is_required_message, FieldValidationError


class BaseField:

    field_type = 'text'

    def __init__(
            self,
            autocomplete='true',
            class_name=None,
            id='',
            label='',
            name='',
            order=0,
            pattern=None,
            placeholder=None,
            required=False,
            value=None,
            wrapper=None,
        ):

        self.autocomplete = autocomplete
        self.class_name = class_name
        self.id = id
        self.label = label
        self.name = name
        self.pattern = pattern
        self.placeholder = placeholder
        self.required = required
        self.order = order
        self.value = value
        self.wrapper = wrapper

    def is_valid(self):
        self.check_required()
        return True

    def check_required(self):

        req_msg = get_field_is_required_message(self.name)

        if self.required is True:

            if self.value is None:
                raise FieldValidationError(
                    field=self.name,
                    message=req_msg
                )

            if len(self.value) == 0:
                raise FieldValidationError(
                    field=self.name,
                    message=req_msg
                )

        return True

    def render_field(self):

        html = '<input '

        html += f'autocomplete="{self.autocomplete}" '

        if self.class_name is not None:
            html += f'class="{self.class_name}" '

        html += f'id="{self.id}" '

        html += f'name="{self.name}" '

        if self.pattern is not None:
            html += f'pattern="{self.pattern}" '

        if self.placeholder is not None:
            html += f'placeholder="{self.placeholder}" '

        if self.required is True:
            html += f'required '

        html += f'type="{self.field_type}" '

        html += f'value="{self.value}" '

        html += '/>'

        return html

    def render_label(self):
        return f'<label for="{self.id}">{self.label}</label>'

    def render_wrapper(self):
        if self.wrapper is None:
            return constants.FIELD_WRAPPER
        return self.wrapper

    def render(self):
        html = self.render_wrapper()
        field = self.render_label()
        field += self.render_field()
        html = re.sub(r'\{\}', field, html)
        return html

    def __repr__(self):
        return self.value
