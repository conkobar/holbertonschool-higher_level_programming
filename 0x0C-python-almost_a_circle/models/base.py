#!/usr/bin/python3
"""module creating base class"""


class Base:
    """base class from which all others in project will stem"""
    __nb_objects = 0

    def __init__(self, id=None):
        """function to init the class"""
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
