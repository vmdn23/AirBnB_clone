#!/usr/bin/python3
"""Users"""


<<<<<<< HEAD
import models
=======

from .base_model import BaseModel
>>>>>>> b67ca62843e7fb50ac73d3fea4d208144c110fbc


class User(models.BaseModel):
    """A user class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Calls super and takes the init of super"""
        super().__init__(**kwargs)

    email = " "
    password = " "
    first_name = " "
    last_name = " "
