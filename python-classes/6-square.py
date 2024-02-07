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

        return self.__size * self.__size  # type: ignore

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):

        return self.__position

    str = "position must be a tuple of 2 positive integers"

    @position.setter
    def position(self, value):

        if not isinstance(value, tuple) or len(value) != 2 \
        or value[0] < 0 or value[1] < 0:
            for x in value:
                if isinstance(x, int):
                    raise TypeError("{str}")
        self.__position = value

    def my_print(self):

        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):  # type: ignore
            print("_" * self.__position[0], end="")
            print("#" * self.__size)  # type: ignore
