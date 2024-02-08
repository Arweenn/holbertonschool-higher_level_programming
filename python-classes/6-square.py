#!/usr/bin/python3
"define a square"


class Square:
    "defining a square"

    __size = None

    @property
    def size(self):
        return self.__size

    def __init__(self, __size=0, __position=(0, 0)):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size
            self.__position = __position

    def area(self):
        "returns the square area"

        return self.__size * self.__size  # type: ignore

    @size.setter
    def size(self, value):
        "getter func for size"

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        "increment my_print func"

        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):  # type: ignore
            print("_" * self.__position[0], end="")
            print("#" * self.__size)  # type: ignore

    @property
    def position(self):
        "define position"

        return self.__position

    @position.setter
    def position(self, value):
        "setter for position property"

        if not isinstance(value, tuple) or len(value) != 2:
            for x in value:
                if not isinstance(x, int):
                    if x < 0:
                        raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
