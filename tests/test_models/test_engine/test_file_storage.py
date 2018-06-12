#!/usr/bin/python3
"""File Storage Test"""
from models.engine.file_storage import FileStorage
import unittest

class Test_FileStorage(unittest.TestCase):
    """
    Test Class FileStorage
    """
    def test_docstring(self):
        """check that docstring exist"""
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_json(self):
        """Raise errors related to JSON conversion"""
        with self.assertRaises(AttributeError):
            FileStorage.__objects
            FileStorage.__File_Path
