#!/usr/bin/python3
"""module creating base class"""


import json


class Base:
    """base class from which all others in project will stem"""
    __nb_objects = 0

    def __init__(self, id=None):
        """function to init the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns json string rep"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return []
