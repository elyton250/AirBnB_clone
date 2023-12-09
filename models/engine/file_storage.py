#!/usr/bin/python3
"""Defines file storage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """represents FileStorage class
    Attributes:
            __file_path (str): The name of the file to save objects to.
            __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key
        Args:
            obj: object to be set
        """
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """serializes __objects to the
        JSON file (path: __file_path)"""

        s_objects = FileStorage.__objects
        s_objects = {obj: s_objects[obj].to_dict() for obj in s_objects.keys()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(s_objects, file)

    def reload(self):
        """deserializes the JSON file to __objects"""

        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for objects in objdict.values():
                    cls_name = objects["__class__"]
                    del objects["__class__"]
                    self.new(eval(cls_name)(**objects))
        except FileNotFoundError:
            return
