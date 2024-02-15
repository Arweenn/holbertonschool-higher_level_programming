#!/usr/bin/python3
"""comment"""


class Student:
    """comment"""

    def __init__(self, first_name, last_name, age):
        """comment"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """comment"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict

    def reload_from_json(self, json):
        """comment"""
        for key in json:
            self.__dict__[key] = json[key]