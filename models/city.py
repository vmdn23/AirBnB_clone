#!/usr/bin/python3
"""City class"""


import models
from models.base_model import BaseModel


class City(BaseModel):
    """A city class that inherits from BaseModel"""
#   state_id = ( string - empty string: it will be the State.id)
    name = " "
