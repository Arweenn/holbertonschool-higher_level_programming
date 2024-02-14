#!/usr/bin/python3
"""comment"""
import json


def load_from_json_file(filename):
    """comment"""

    with open(filename, "r") as f:
        return json.load(f)
