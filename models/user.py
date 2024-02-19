#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import storage_type


class User(BaseModel, Base):
    """This class defines a user by various attributes
       __tablename__: users mapping table
        email: sqlalchemy String column: the user's entered email
        password: sqlalchemy String column: the user's entered password
        first_name: sqlalchemy String column: the user's firstname
        last_name: sqlalchemy String column: the user's lastname"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    if storage_type != 'db':
        email = ''
        password = ''
        first_name = ''
        last_name = ''
