#!/usr/bin/python3
"""class rectangle"""
from models.base import Base

class Rectangle(Base):
    """class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def __width(self):
        return self.__width

    @__width.setter
    def __width(self, value):
        self.__width = value

    @property
    def __height(self):
        return self.__height

    @__height.setter
    def __height(self, value):
        self.__height = value

    @property
    def __x(self):
        return self.__x

    @__x.setter
    def __x(self, value):
        self.__x = value

    @property
    def __y(self):
        return self.__y

    @__y.setter
    def __y(self, value):
        self.__y = value
