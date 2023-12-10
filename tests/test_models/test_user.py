#!/usr/bin/python3
"""this module tests the user class"""


import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """this class contains methods"""

    def test_attributes(self):
        """Test that the User class has the expected attributes."""
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_str_representation(self):
        """Test the __str__ method of the User class."""
        user = User()
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

if __name__ == '__main__':
    unittest.main()

