#!/usr/bin/python3
""" find if obj is in instance of given class """


def is_same_class(obj, a_class):
    """ returns true or false """
    if type(obj) == a_class:
        return True
    else:
        return False
