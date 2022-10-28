from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from uvicorn_framework.database.models import Model

from .. import constants


class User(Model):

    __tablename__ = constants.TABLE_NAME_USERS

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)


class Project(Model):

    __tablename__ = constants.TABLE_NAME_PROJECTS

    id = Column(Integer, primary_key=True)


class Tenant(Model):

    __tablename__ = constants.TABLE_NAME_TENANTS

    id = Column(Integer, primary_key=True)


class ProjectAdmin(Model):

    __tablename__ = constants.TABLE_NAME_PROJECT_ADMINS

    id = Column(Integer, primary_key=True)

    project_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_PROJECTS}.id'))
    user_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_USERS}.id'))

    project = relationship('Project', back_populates='admins', cascade=Model.CASCADE_REMOVE_ALL)
    user = relationship('User', back_populates='projects', cascade=Model.CASCADE_REMOVE_ALL)


class ProjectTenant(Model):

    __tablename__ = constants.TABLE_NAME_PROJECT_TENATS

    id = Column(Integer, primary_key=True)

    project_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_PROJECTS}.id'))
    tenant_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_TENANTS}.id'))

    project = relationship('Project', back_populates='tenants', cascade=Model.CASCADE_REMOVE_ALL)
    tenant = relationship('Tenant', back_populates='projects', cascade=Model.CASCADE_REMOVE_ALL)


class TenantUser(Model):

    __tablename__ = constants.TABLE_NAME_TENANT_USERS

    id = Column(Integer, primary_key=True)
    acl = Column(String, nullable=True, server_default='user')

    tenant_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_TENANTS}.id'))
    user_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_USERS}.id'))

    tenant = relationship('Tenant', back_populates='users', cascade=Model.CASCADE_REMOVE_ALL)
    user = relationship('User', back_populates='tenants', cascade=Model.CASCADE_REMOVE_ALL)


class Item(Model):

    __tablename__ = constants.TABLE_NAME_ITEMS

    id = Column(Integer, primary_key=True)
    content_type = Column(String)

    project_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_PROJECTS}.id'))
    tenant_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_TENANTS}.id'))

    project = relationship('Project', back_populates='items', cascade=Model.CASCADE_REMOVE_ALL)
    tenant = relationship('Tenant', back_populates='items', cascade=Model.CASCADE_REMOVE_ALL)


class Content(Model):

    __tablename__ = constants.TABLE_NAME_TRANSLATABLE_CONTENTS

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey(f'{constants.TABLE_NAME_ITEMS}.id'))

    item = relationship('Item', back_populates='translatable_contents', cascade=Model.CASCADE_REMOVE_ALL)
