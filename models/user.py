#!/usr/bin/python3
"""Defines a user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user class
    Args:
        email: user email
        password: password of the email
        first_name: first name of the user
        last_name: last_name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
