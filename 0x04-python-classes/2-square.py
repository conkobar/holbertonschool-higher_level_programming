#!/usr/bin/python3
""" expanding on existing square class """


class Square:
    """ further attributes given to the square """

    def __init__(self, size=0):
        """ size must be int and > 0 """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ return the area of the square """
        return self.__size ** 2
