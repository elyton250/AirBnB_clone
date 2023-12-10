#!/usr/bin/python3
"""this module tests review module"""


import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """this class test the review module"""

    def test_attributes(self):
        """Test that the Review class has the expected attributes."""
        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_str_representation(self):
        """Test the __str__ method of the Review class."""
        review = Review()
        expected_str = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(str(review), expected_str)

if __name__ == '__main__':
    unittest.main()

