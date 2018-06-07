#!/usr/bin/python3
"""Class BaseModel"""


import uuid
from datetime import datetime
import json


class BaseModel:
    """Base Class with public instance attributes and methods"""


    def __init__(self, id=None, created_at="", updated_at=""):
    	"""Instantiates the attributes of the BaseModel class"""
    	if id is not None:
    		self.id = id
    	else:
    		self.id = str(uuid.uuid4())
    		self.created_at = datetime.now()
    		self.updated_at = datetime.now()


    def __str__(self):
    	""" Return the human readable print format"""
    	a, b = self.id, self.__dict__
    	return("[BaseModel] ({}) {}".format(a, b))

    def save(self):
    	"""Shows the newly updated time from time of instance creation"""
    	self.updated_at = datetime.now()

    def to_dict(self):
    	"""Returns a dictionay containing all keys/values"""
    	pass