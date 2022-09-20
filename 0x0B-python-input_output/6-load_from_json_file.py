#!/usr/bin/python3
"""more json stuff"""
import json


def load_from_json_file(filename):
    """turns json file into object"""
    with open(filename) as f:
        return json.loads(f.read())
