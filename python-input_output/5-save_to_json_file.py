#!/usr/bin/python3
"""comment"""
import json


def save_to_json_file(my_obj, filename):
    """comment"""

    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
