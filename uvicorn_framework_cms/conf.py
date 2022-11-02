from uvicorn_framework.database.models import Model
from uvicorn_framework.routers import route

from .admin.viewsets.project_tenant_item import ProjectTenantItemViewSet
from .admin.viewsets.project_tenant_items import ProjectTenantItemsViewSet
from .admin.viewsets.project_tenant_user import ProjectTenantUserViewSet
from .admin.viewsets.project_tenant_users import ProjectTenantUsersViewSet

from .admin.viewsets.project_tenant import ProjectTenantViewSet
from .admin.viewsets.project_tenants import ProjectTenantsViewSet

from .admin.viewsets.project import ProjectViewSet
from .admin.viewsets.projects import ProjectsViewSet

from .admin.viewsets.tenant import TenantViewSet
from .admin.viewsets.tenants import TenantsViewSet

from .admin.viewsets.profile import ProfileViewSet

from .admin.viewsets.register import RegisterViewSet
from .admin.viewsets.sign_in import SignInViewSet
from .admin.viewsets.sign_out import SignOutViewSet

from . import constants

from .database.models import CMSModel
from .database.models import User

from .http.requests import Request


class Settings:

    SESSION_COOKIE_NAME = 'session_id'

    def DB_MIGRATE(self, engine):
        CMSModel.metadata.create_all(engine.engine)

    def CREATE_SUPERUSER(self, cursor, email, password):
        user = self.CREATE_USER(cursor, email, password, True)
        return user

    def CREATE_USER(self, cursor, email, password, is_superuser=False):
        user = User(email=email, password=password, is_superuser=is_superuser)
        cursor.add(user)
        cursor.commit()
        return user

    def extend(self, base_settings):

        base_settings.REQUEST_CLASS = Request

        base_settings.ROUTES += [

            # Project tenant users
            route(
                r'/cms/projects/(?P<project_id>[0-9]+)/tenants/(?P<tenant_id>[0-9]+)/users/(?P<id>[0-9]+)/',
                ProjectTenantUserViewSet,
                'cms_project_tenant_user'
            ),
            route(
                r'/cms/projects/(?P<project_id>[0-9]+)/tenants/(?P<tenant_id>[0-9]+)/users/',
                ProjectTenantUsersViewSet,
                'cms_project_tenant_users'
            ),

            # Project tenants items
            route(
                r'/cms/projects/(?P<project_id>[0-9]+)/tenants/(?P<tenant_id>[0-9]+)/(?P<ct_name>[0-9a-zA-Z\-\_]+)/(?P<id>[0-9]+)/',
                ProjectTenantItemViewSet,
                'cms_project_tenant_item'
            ),
            route(
                r'/cms/projects/(?P<project_id>[0-9]+)/tenants/(?P<tenant_id>[0-9]+)/(?P<ct_name>[0-9a-zA-Z\-\_]+)/',
                ProjectTenantItemsViewSet,
                'cms_project_tenant_items'
            ),

            # Project tenants
            route(
                r'/cms/projects/(?P<project_id>[0-9]+)/tenants/(?P<id>[0-9]+)/',
                ProjectTenantViewSet,
                'cms_project_tenant'
            ),
            route(
                r'/cms/projects/(?P<project_id>[0-9]+)/tenants/',
                ProjectTenantsViewSet,
                'cms_project_tenants'
            ),

            # Projects
            route(
                r'/cms/projects/(?P<id>[0-9]+)/',
                ProjectViewSet,
                'cms_project'
            ),
            route(
                r'/cms/projects/',
                ProjectsViewSet,
                'cms_projects'
            ),

            # Tenants
            route(
                r'/cms/tenants/(?P<id>[0-9]+)/',
                TenantViewSet,
                constants.URLNAME_CMS_TENANT
            ),
            route(
                r'/cms/tenants/',
                TenantsViewSet,
                'cms_tenants'
            ),

            # Profile
            route(
                r'/cms/profile/',
                ProfileViewSet,
                'cms_user_profile'
            ),

            # Auth
            route(
                r'/cms/sign-out/',
                SignOutViewSet,
                constants.URLNAME_CMS_SIGN_OUT
            ),
            route(
                r'/cms/register/',
                RegisterViewSet,
                constants.URLNAME_CMS_REGISTER
            ),
            route(
                r'/cms/',
                SignInViewSet,
                constants.URLNAME_CMS_SIGN_IN
            ),
        ]

        base_settings.SESSION_COOKIE_NAME = self.SESSION_COOKIE_NAME


settings = Settings()
