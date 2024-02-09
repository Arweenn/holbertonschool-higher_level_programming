#!/usr/bin/python3
"""function that prints a string"""


def say_my_name(first_name, last_name=""):
    """func definition"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
