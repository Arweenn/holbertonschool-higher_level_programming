#!/usr/bin/python3
"""writing the first class Base"""
import json


class Base:
    """first class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
