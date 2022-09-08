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

    def my_print(self):
        # print the square as pound signs
        box = range(self.size)

        # print empty line if there is no square
        if box:
            for i in box:
                for j in box:
                    print("#", end="")
                print()
        else:
            print()

    @property
    def size(self):
        # returns the square's size
        return self.__size

    @size.setter
    def size(self, value):
        # sets the size of the square
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
