#!/usr/bin/python3
"""writing the first class Base"""


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
