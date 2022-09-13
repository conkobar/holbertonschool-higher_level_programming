#!/usr/bin/python3
""" another square printing function """


def print_square(size):
    """ prints a square with @size """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    if size:
        for i in range(size):
            for n in range(size):
                print("#", end="")
            print()
