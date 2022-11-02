from uvicorn_framework.conf import settings
from jinja2 import Template

from .. import constants

from ..http.resolvers import reverse

from .base import StandaloneTag


class MainMenuExtension(StandaloneTag):

    _template = 'uvicorn_framework_cms/admin/components/mainmenu.html'
    tags = ['mainmenu', ]

    def render(self):

        request = self.context['request']

        context = {
            'request': request,
            'links': [],
        }

        if request.user is None:
            context['links'].append({
                'href': reverse(constants.URLNAME_CMS_SIGN_IN),
                'text': 'Sign in'
            })
        else:
            context['links'].append({
                'href': reverse(constants.URLNAME_CMS_PROJECTS),
                'text': 'Projects'
            })
            context['links'].append({
                'href': '',
                'text': request.user.email,
                'children': [
                    {
                        'href': '',
                        'text': 'Profile'
                    },
                    {
                        'href': reverse(constants.URLNAME_CMS_SIGN_OUT),
                        'text': 'Sign out'
                    }
                ]
            })

        template = settings.TEMPLATE_ENGINE.environment.get_template(
            self._template
        )

        return template.render(**context)
