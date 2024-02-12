#!/usr/bin/python3
'''This module defines a User class'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Class for creating user objects'''

    first_name = ''
    last_name = ''
    email = ''
    password = ''
