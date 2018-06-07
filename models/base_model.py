#!/usr/bin/python3
"""Class BaseModel"""


import uuid
from datetime import datetime
import json


class BaseModel:
    """Base Class with public instance attributes and methods"""


    def __init__(self, id=None, created_at="", updated_at=""):
    	"""Instantiates the attributes of the BaseModel class"""
    	self.id = str(uuid.uuid4())
    	self.created_at = datetime.now()
    	self.updated_at = datetime.now()
    	self.save()


    def __str__(self):
    	""" Return the human readable print format"""
    	a, b, c = self.__class__.__name__, self.id, self.__dict__
    	return("[{}] ({}) {}".format(a, b, c))

    def save(self):
    	"""Shows the newly updated time from time of instance creation"""
    	self.updated_at = datetime.utcnow()

    def to_dict(self):
    	"""Returns a dictionay containing all keys/values"""
    	my_dict = {}
    	for key, item in self.__dict__.items():
    		if key in ['created_at', 'updated_at']:
    			my_dict[key] = item.isoformat()
    		else:
    			my_dict[key] = item
    	my_dict['__class__'] = self.__class__.__name__
    	return my_dict