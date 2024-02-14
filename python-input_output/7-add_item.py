#!/usr/bin/python3
"""comment"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv[1:]
filename = "add_item.json"
with open(filename, "a+") as f:
    try:
        my_list = load_from_json_file(filename)
    except Exception:
        my_list = []
    my_list.extend(args)
    save_to_json_file(my_list, filename)
