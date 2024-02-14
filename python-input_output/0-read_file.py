#!/usr/bin/python3
"""comment"""


def read_file(filename=""):
    """comment"""

    with open(filename, "r") as f:
        for line in f:
            print(line, end="")
