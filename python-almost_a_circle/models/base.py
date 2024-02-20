#!/usr/bin/python3
"""writing the first class Base"""
import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            json_str = cls.to_json_string([obj.to_dictionary()
                                           for obj in list_objs])
            f.write(json_str)
