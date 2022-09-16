#!/usr/bin/python3
"""empty class per given task"""


from multiprocessing.sharedctypes import Value


class BaseGeometry:
    """new class per given task"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
