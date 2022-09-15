#!/usr/bin/python3
"""checks for objects inheritance"""


def inherits_from(obj, a_class):
    """returns True or False"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
