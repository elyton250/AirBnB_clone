#!/usr/bin/python3
"""this modules tests the file storage"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
"""from models.city import City"""
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage

class TestFileStorage(unittest.TestCase):
    """this class tests the file storing object"""
    def setUp(self):
        """sets up the resources to be used"""
        self.storage = storage
        path, objects = self.storage.access()
        self.objects = objects
        self.path = path

    def tearDown(self):
        """removes the created file path"""
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_all(self):
        """tests the all method"""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, self.objects)

    def test_new(self):
        """tests the creation method new"""
        model = BaseModel()
        self.storage.new(model)
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.objects)
        self.assertEqual(self.objects[key], model)

    def test_save_and_reload(self):
        """test the methods that saves to a json file"""
        model1 = BaseModel()
        (self.storage.new(model1))
        self.storage.save()
        self.storage.reload()
        self.assertEqual(self.storage.save(), self.storage.reload())

if __name__ == '__main__':
    unittest.main()

