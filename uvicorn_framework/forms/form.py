import inspect
import re

from markupsafe import Markup

from ..constants import FIELD_NAME_CSRF_TOKEN

from .exceptions import FieldValidationError, FormValidationError
from .fields.base import BaseField


class BaseForm:

    def __init__(
            self,
            action='',
            method='',
            csrf_token=None,
            template=None,
            class_names='',
            data={},
        ):

        self._fields = None

        self.action = action
        self.data = data
        self.method = method
        self.csrf_token = csrf_token
        self.template = template
        self.class_names = class_names

    def is_valid(self):

        fields = self.get_form_fields()
        errors = {}

        for key, field in fields.items():

            try:
                print('Validating field:', key, field)
                field.is_valid()
            except FieldValidationError as e:
                errors[e.field] = e.message

        if errors != {}:
            raise FormValidationError(
                errors=errors,
                message='Form is invalid'
            )

        return True

    def get_form_fields(self):

        if self._fields is not None:
            return self._fields

        fields = {}

        for key, field in inspect.getmembers(self):
            if key.startswith('__') is False and key.endswith('__') is False:
                if isinstance(field, BaseField) is True:
                    if key in self.data:
                        field.name = key
                        field.value = self.data[key]
                    fields[key] = field

        self._fields = fields

        return self._fields

    def render_form(self):
        html = '<form '
        html += f'action="{self.action}" '
        html += f'method="{self.method}" '
        html += f'class="{self.class_names}" '
        html += '>{}</form>'
        return html

    def render_csrf_token(self):

        if self.csrf_token is None:
            return ''

        html = '<input '
        html += 'type="hidden" '
        html += f'name="{FIELD_NAME_CSRF_TOKEN}" '
        html += f'value="{self.csrf_token}" '
        html += '/>'

        return html

    def render(self):

        html = self.render_form()
        field_htmls = []

        fields = self.get_form_fields()

        for name, field in fields.items():
            field_htmls.append([field.order, field.render()])

        field_htmls.sort(key=lambda x: x[0])

        field_htmls = list(map(lambda x: x[1], field_htmls))

        field_html = self.render_csrf_token() + ''.join(field_htmls)

        html = re.sub(r'\{\}', field_html, html)

        return Markup(html)
