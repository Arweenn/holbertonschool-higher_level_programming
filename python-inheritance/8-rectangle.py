#!/usr/bin/python3
"""comment"""


class BaseGeometry:
    """comment"""

    def __init__(self, width, height):
        """comment"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height

    def area(self):

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """comment"""

        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
