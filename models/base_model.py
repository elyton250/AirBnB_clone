#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from datetime import datetime
import uuid


class BaseModel:
    """Repsents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """initializes a base model
        Args:
            *args: unused
            **kwargs: Key/value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        isof = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key.endswith('at') and isinstance(value, str):
                    self.__dict__[key] = datetime.strptime(value, isof)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """updates update_at attribute with current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        i_dict = self.__dict__.copy()
        i_dict["created_at"] = self.created_at.isoformat()
        i_dict["updated_at"] = self.updated_at.isoformat()
        i_dict['__class__'] = self.__class__.__name__
        return (i_dict)

    def __str__(self):
        """prints Base_model instances"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
