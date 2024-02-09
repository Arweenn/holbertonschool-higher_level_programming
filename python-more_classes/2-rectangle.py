#!/usr/bin/python3
"""empty class"""


class Rectangle:
    """defining a rectangle"""

    def __init__(self, width=0, height=0):
        """This method constructs the object"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

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

    def area(self):
        """func definition"""

        return self.width * self.height

    def perimeter(self):
        """func definition"""

        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)
