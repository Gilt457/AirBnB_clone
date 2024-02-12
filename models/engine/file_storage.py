#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os

# Importing the models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Class for storing and retrieving data"""
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary of objects

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            # Convert objects to dictionaries
            d = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, f)  # Write to file

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        return {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    def reload(self):
        """Reloads the stored objects"""
        if os.path.exists(self.__file_path):  # Check if file exists
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)  # Load from file
                # Create objects from dictionaries
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
                # TODO: should this overwrite or insert?
                self.__objects = obj_dict

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        return {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State": {
                "name": str
            },
            "City": {
                "state_id": str,
                "name": str
            },
            "Amenity": {
                "name": str
            },
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
