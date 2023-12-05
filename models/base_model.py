#!/usr/bin/python3
import datetime
import json
import uuid

class BaseModel:
    def __init__(self, id=None, *args, **kwargs):
        self.id = str(uuid.uuid4())
        if kwargs:
            self.from_dict(kwargs)
        else:              
            self.created_at = self.isoformat(datetime.datetime.now())
            self.updated_at = self.isoformat(datetime.datetime.now())
    def save(self):
        self.updated_at = self.isoformat(datetime.datetime.now())
    def to_dict(self):
        i_dict = self.__dict__
        i_dict['__class__'] = self.__class__.__name__
        return i_dict
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    def to_json(self):
        return json.dumps(self.to_dict())
    @staticmethod
    def isoformat(dt):
        return dt.isoformat()
    @classmethod
    def from_dict(cls, kwargs):
        """instance = cls()"""
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            if key.endswith('at') and isinstance(value, str):
                setattr(self, key, datetime.datetime.fromisoformat(value))
            else:
                setattr(self, key, value)
