#!/usr/bin/python3
"""
Unittest for user_model
"""
import unittest
import sys
from io import StringIO
from models.user import User
import pep8


class Test_User(unittest.TestCase):
    """
    Test class User
    """
    def test_docstring(self):
        """check that docstring exist"""
        self.assertTrue(len(User.__doc__) > 1)
        self.assertTrue(len(User.__init__.__doc__) > 1)
        self.assertTrue(len(User.__str__.__doc__) > 1)
        self.assertTrue(len(User.save.__doc__) > 1)
        self.assertTrue(len(User.to_dict.__doc__) > 1)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

    def setUp(self):
        """
        redirect stdout of the output for functions using print
        """
        sys.stdout = StringIO

    def tearDown(self):
        """
        re-establish the stdout back to normal after setUp
        """
        sys.stdout = sys.__stdout__

    def test_init_arg(self):
        """pass in arg to new instance"""
        b0 = User(12)
        self.assertEqual(type(b0).__name__, "User")
        self.assertFalse(hasattr(b0, "12"))

    def test_init_kwarg(self):
        """pass in kwargs to instance"""
        b00 = User(name="Tehe")
        self.assertEqual(type(b00).__name__, "User")
        self.assertTrue(hasattr(b00, "name"))
        self.assertFalse(hasattr(b00, "id"))
        self.assertFalse(hasattr(b00, "created_at"))
        self.assertFalse(hasattr(b00, "updated_at"))
        self.assertTrue(hasattr(b00, "__class__"))

    def test_init_argfail(self):
        """init arg should fail"""
        b000 = User()

    def test_before_todict(self):
        """test instances before method todict conversion"""
        b1 = User()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "User")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.user.User'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')

    def test_after_todict(self):
        """test instances after method to_dict conversion"""
        my_model = User()
        new_model = User()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, User)
        self.assertEqual(type(my_model).__name__, "User")
        self.assertEqual(test_dict['__class__'], "User")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_str_method(self):
        """test that each method is printing accurately"""
        b3 = User()
        b3printed = b3.__str__()
        self.assertEqual(b3printed,
                         "[User] ({}) {}".format(b3.id, b3.__dict__))

    def test_hasattribute(self):
        """test that instance of Base have been correctly made"""
        b2 = User()
        self.assertTrue(hasattr(b2, "__init__"))
        self.assertTrue(hasattr(b2, "created_at"))
        self.assertTrue(hasattr(b2, "updated_at"))
        self.assertTrue(hasattr(b2, "id"))
