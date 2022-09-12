#!/usr/bin/python3
""" adds two numbers together """


def add_integer(a, b=98):
    """ adds two ints/floats; returns int """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
