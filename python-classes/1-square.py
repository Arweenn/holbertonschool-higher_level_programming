#!/usr/bin/python3
"class defining a square"

class Square:
    "class defining a square"

    __size = None

    def __init__(self, __size):
        if isinstance(__size, int):
            self.__size = __size
        else:
            return None
