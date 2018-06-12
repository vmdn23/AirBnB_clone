#!/usr/bin/python3
"""This is a  module of unittest cases for BaseModel class
"""

import unittest
import json
from models.base_model import BaseModel
from io import StringIO
import sys
import os
import pep8


class TestBaseModel(unittest.TestCase):
    """Class that contain functions to run tests
    """

    def test_uuid(self):
        """Tests the Universal Unique Identifier of a class
        """
        bm1 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        selfassertTrue(hasattr(bm, "id")
