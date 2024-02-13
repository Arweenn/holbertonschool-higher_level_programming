#!/usr/bin/python3
"""comment"""


def inherits_from(obj, a_class):
    """comment"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
