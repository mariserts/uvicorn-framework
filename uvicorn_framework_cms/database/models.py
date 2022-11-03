import uuid

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from uvicorn_framework.database.models import Model

from .. import constants


class CMSModel(Model):

    __abstract__ = True


class SessionModel(CMSModel):

    __tablename__ = constants.TABLE_NAME_SESSIONS

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(Integer, nullable=True)


class UserModel(CMSModel):

    __tablename__ = constants.TABLE_NAME_USERS

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    is_superuser = Column(Boolean, default=False)


class ProjectModel(CMSModel):

    __tablename__ = constants.TABLE_NAME_PROJECTS

    id = Column(Integer, primary_key=True)


class TenantModel(CMSModel):

    __tablename__ = constants.TABLE_NAME_TENANTS

    id = Column(Integer, primary_key=True)


class ProjectAdminModel(CMSModel):

    __tablename__ = constants.TABLE_NAME_PROJECT_ADMINS

    id = Column(Integer, primary_key=True)

    project_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_PROJECTS}.id'))
    user_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_USERS}.id'))

    project = relationship('ProjectModel', foreign_keys='ProjectAdminModel.project_id')
    user = relationship('UserModel', foreign_keys='ProjectAdminModel.user_id')


class ProjectTenantModel(CMSModel):

    __tablename__ = constants.TABLE_NAME_PROJECT_TENANTS

    id = Column(Integer, primary_key=True)

    project_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_PROJECTS}.id'))
    tenant_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_TENANTS}.id'))

    project = relationship('ProjectModel', foreign_keys='ProjectTenantModel.project_id')
    tenant = relationship('TenantModel', foreign_keys='ProjectTenantModel.tenant_id')


class TenantUserModel(CMSModel):

    __tablename__ = constants.TABLE_NAME_TENANT_USERS

    id = Column(Integer, primary_key=True)
    acl = Column(String, nullable=True, default='user')

    tenant_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_TENANTS}.id'))
    user_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_USERS}.id'))

    tenant = relationship('TenantModel', foreign_keys='TenantUserModel.tenant_id')
    user = relationship('UserModel', foreign_keys='TenantUserModel.user_id')


class ItemModel(CMSModel):

    __tablename__ = constants.TABLE_NAME_ITEMS

    id = Column(Integer, primary_key=True)
    content_type = Column(String)

    project_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_PROJECTS}.id'))
    tenant_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_TENANTS}.id'))

    project = relationship('ProjectModel', foreign_keys='ItemModel.project_id')
    tenant = relationship('TenantModel', foreign_keys='ItemModel.tenant_id')


class ContentModel(CMSModel):

    __tablename__ = constants.TABLE_NAME_TRANSLATABLE_CONTENTS

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_ITEMS}.id'))

    item = relationship('ItemModel', foreign_keys='ContentModel.item_id')
