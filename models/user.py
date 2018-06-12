#!/usr/bin/python3
"""Users"""


import models


class User(models.BaseModel):
    """A user class that inherits from BaseModel"""
    email = " "
    password = " "
    first_name = " "
    last_name = " "
