#!/usr/bin/python3
"""Users"""



from .base_model import BaseModel


class User(BaseModel):
    """A user class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Calls super and takes the init of super"""
        super().__init__(**kwargs)

    email = " "
    password = " "
    first_name = " "
    last_name = " "
