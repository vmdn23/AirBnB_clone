#!/usr/bin/python3
"""Review class"""


import models
from models.base_model import BaseModel


class Review(BaseModel):
    """A review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
