#!/usr/bin/python3
"""comment"""


class BaseGeometry:
    """empty class"""

    def area(self):

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """comment"""

        if not type(value) is int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
