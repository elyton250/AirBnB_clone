#!/usr/bin/python3
"""this modules test state class"""


import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_attributes(self):
        """Test that the State class has the expected attributes."""
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_str_representation(self):
        """Test the __str__ method of the State class."""
        state = State()
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)

if __name__ == '__main__':
    unittest.main()
