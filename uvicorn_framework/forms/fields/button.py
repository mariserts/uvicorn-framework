import re

from ... import constants

from .base import BaseField


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
