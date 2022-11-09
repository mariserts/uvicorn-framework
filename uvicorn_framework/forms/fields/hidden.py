from .base import BaseField


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

    def render(self):
        return self.render_field()
