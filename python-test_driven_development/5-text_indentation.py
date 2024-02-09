#!/usr/bin/python3
"""function that prints a text"""


def text_indentation(text):
    """func definition"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""

    for i in text:
        if i == " " and len(new_text) == 0:
            continue
        elif i == " " and new_text[-1] in "\n":
            continue
        new_text += i
        if i in ".?:!":
            new_text += "\n\n"

    print(new_text, end="")
