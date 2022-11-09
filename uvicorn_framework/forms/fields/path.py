from urllib.parse import urlparse

from ..exceptions import get_field_is_message, FieldValidationError

from .url import URLField


class PathField(URLField):

    field_type = 'text'

    def is_valid(self):

        not_path_msg = get_field_is_message(
            self.name,
            'is not a valid path'
        )

        self.check_required()

        if self.value is not None:

            if '/' not in self.value
                if '.' not in self.value:
                    raise FieldValidationError(
                        field=self.name,
                        message=not_path_msg
                    )

            # Check if path doesnt have other non path chars
            # like asterix, pipe etc
            # print('TODO: PathField special char validation')

        return True
