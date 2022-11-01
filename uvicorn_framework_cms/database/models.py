import uuid

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from uvicorn_framework.database.models import Model

from .. import constants


class CMSModel(Model):

    __abstract__ = True


class Session(CMSModel):

    __tablename__ = constants.TABLE_NAME_SESSIONS

    id = Column(String, primary_key=True, server_default=str(uuid.uuid4()))
    user_id = Column(Integer, nullable=True)


class User(CMSModel):

    __tablename__ = constants.TABLE_NAME_USERS

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    is_superuser = Column(Boolean, server_default=False)


class Project(CMSModel):

    __tablename__ = constants.TABLE_NAME_PROJECTS

    id = Column(Integer, primary_key=True)


class Tenant(CMSModel):

    __tablename__ = constants.TABLE_NAME_TENANTS

    id = Column(Integer, primary_key=True)


class ProjectAdmin(CMSModel):

    __tablename__ = constants.TABLE_NAME_PROJECT_ADMINS

    id = Column(Integer, primary_key=True)

    project_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_PROJECTS}.id'))
    user_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_USERS}.id'))

    project = relationship('Project', foreign_keys='ProjectAdmin.project_id')
    user = relationship('User', foreign_keys='ProjectAdmin.user_id')


class ProjectTenant(CMSModel):

    __tablename__ = constants.TABLE_NAME_PROJECT_TENANTS

    id = Column(Integer, primary_key=True)

    project_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_PROJECTS}.id'))
    tenant_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_TENANTS}.id'))

    project = relationship('Project', foreign_keys='ProjectTenant.project_id')
    tenant = relationship('Tenant', foreign_keys='ProjectTenant.tenant_id')


class TenantUser(CMSModel):

    __tablename__ = constants.TABLE_NAME_TENANT_USERS

    id = Column(Integer, primary_key=True)
    acl = Column(String, nullable=True, server_default='user')

    tenant_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_TENANTS}.id'))
    user_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_USERS}.id'))

    tenant = relationship('Tenant', foreign_keys='TenantUser.tenant_id')
    user = relationship('User', foreign_keys='TenantUser.user_id')


class Item(CMSModel):

    __tablename__ = constants.TABLE_NAME_ITEMS

    id = Column(Integer, primary_key=True)
    content_type = Column(String)

    project_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_PROJECTS}.id'))
    tenant_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_TENANTS}.id'))

    project = relationship('Project', foreign_keys='Item.project_id')
    tenant = relationship('Tenant', foreign_keys='Item.tenant_id')


class Content(CMSModel):

    __tablename__ = constants.TABLE_NAME_TRANSLATABLE_CONTENTS

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_ITEMS}.id'))

    item = relationship('Item', foreign_keys='Content.item_id')
