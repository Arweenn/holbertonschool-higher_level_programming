#!/usr/bin/python3
"""comment"""


def read_file(filename=""):
    """comment"""

    with open('my_file_0.txt', 'r') as f:
        for line in f:
            print(line, end="")
