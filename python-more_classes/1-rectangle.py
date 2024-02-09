#!/usr/bin/python3
"""empty class"""


class Rectangle:
    """defining a rectangle"""

    def __init__(self, width=0, height=0):
        """This method constructs the object"""

        if isinstance(width, int) and isinstance(height, int):
            self.__width = width
            self.__height = height

    @property
    def width(self):
        """func defintion"""

        return self.__width

    @width.setter
    def width(self, value):
        """func defintion"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """func defintion"""

        return self.__height

    @height.setter
    def height(self, value):
        """func defintion"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
