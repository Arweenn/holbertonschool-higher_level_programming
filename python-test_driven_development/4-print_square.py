#!/usr/bin/python3
"""function that prints a square"""


def print_square(size):
    """func definition"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
