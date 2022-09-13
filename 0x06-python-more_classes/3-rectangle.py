#!/usr/bin/python3
""" make a rectangle out of given values """


class Rectangle:
    """ class to construct a rectangle """
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if 0 in (self.__height, self.__width):
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width and self.__height:
            return ("\n".join(
                "#" * self.__width for i in range(
                    self.__height)))
        else:
            return ""

    def __repr__(self):
        return ("{}({}, {})".format(
            self.__class__.__name__,
            self.__width,
            self.__height))
