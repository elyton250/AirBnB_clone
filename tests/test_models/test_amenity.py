#!/bin/python3
"""this modules tests amenity"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """this class contains the test methods"""

    def test_attributes(self):
        """Test that the Amenity class has the expected attributes."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "2")

    def test_str_representation(self):
        """Test the __str__ method of the Amenity class."""
        amenity = Amenity()
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)

    def test_to_dict_method(self):
        """Test the to_dict method of the Amenity class."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertTrue(isinstance(amenity_dict, dict))
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], amenity.id)
        self.assertEqual(amenity_dict['created_at'], amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'], amenity.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
