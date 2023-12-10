#!/usr/bin/python3
"""this class tests the city class"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """this test is for tests attribute creation and contents"""

    def test_attributes(self):
        """Test that the City class has the expected attributes."""
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_str_representation(self):
        """Test the __str__ method of the City class."""
        city = City()
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)

if __name__ == '__main__':
    unittest.main()
