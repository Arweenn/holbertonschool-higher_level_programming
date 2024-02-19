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
