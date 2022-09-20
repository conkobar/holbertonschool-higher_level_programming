#!/usr/bin/python3
"""writes to txt file using json"""
import json


def save_to_json_file(my_obj, filename):
    """writes to file using json formatting"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
