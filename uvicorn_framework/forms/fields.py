import re

from .. import constants

from ..validators.emails import email_is_valid
from ..validators.passwords import password_is_valid


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
            placeholder='',
            required=False,
            value='',
            wrapper=None,
        ):

        self.autocomplete = autocomplete
        self.class_name = class_name
        self.id = id
        self.label = label
        self.name = name
        self.order = order
        self.placeholder = placeholder
        self.required = required
        self.value = value
        self.wrapper = wrapper

    def is_valid(self):
        return False

    def render_field(self):

        html = '<input '

        html += f'autocomplete="{self.autocomplete}" '

        if self.class_name is not None:
            html += f'class="{self.class_name}" '

        html += f'id="{self.id}" '

        html += f'name="{self.name}" '

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


class Button(BaseField):

    def __init__(
            self,
            class_name=None,
            label='',
            name=None,
            order=0,
            value=None,
            wrapper=None,
        ):

        self.class_name = class_name
        self.label = label
        self.name = name
        self.order = order
        self.value = value
        self.wrapper = wrapper

    def is_valid(self):
        return True

    def render_wrapper(self):
        if self.wrapper is None:
            return constants.FIELD_WRAPPER
        return self.wrapper

    def render_button(self):

        html = '<button '

        if self.class_name is not None:
            html += f'class="{self.class_name}" '

        if self.name is not None:
            html += f'name="{self.name}" '

        if self.value is not None:
            html += f'value="{self.value}" '

        html += f'>{self.label}</button>'

        return html

    def render(self):
        html = self.render_wrapper()
        field = self.render_button()
        html = re.sub(r'\{\}', field, html)
        return html


class EmailField(BaseField):

    field_type = 'email'

    def is_valid(self):
        return email_is_valid(self.value)


class HiddenField(BaseField):

    field_type = 'hidden'

    def is_valid(self):
        return True

    def render_field(self):

        html = '<input '

        html += f'name="{self.name}" '

        if self.placeholder is not None:
            html += f'placeholder="{self.placeholder}" '

        html += f'type="{self.field_type}" '

        html += f'value="{self.value}" '

        html += '/>'

        return html


class PasswordField(BaseField):

    field_type = 'password'

    def is_valid(self):
        return password_is_valid(self.value)
