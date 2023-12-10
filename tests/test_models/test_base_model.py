#!/usr/bin/python3
"""
this modules tests the base_models
"""


import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """this class test the base_model"""

    def test_init(self):
        """this method tests the initialisation"""
        
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_save(self):
        """this method tests the save method"""
        
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict(self):
        """this method saves the to dict method"""
        
        model = BaseModel()
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_str(self):
        """this method tests the string representation"""
        
        model = BaseModel()
        str_representation = str(model)

        self.assertIsInstance(str_representation, str)
        self.assertIn(model.id, str_representation)
        self.assertIn(model.__class__.__name__, str_representation)

if __name__ == '__main__':
    unittest.main()

