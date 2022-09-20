#!/usr/bin/python3
"""module for rectangular model"""
from models.base import Base


class Rectangle(Base):
    """defining rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing rectangle class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """placeholder for future comments"""
        return self.__width

    @width.setter
    def width(self, width):
        """placeholder for future comments"""
        self.__width = width

    @property
    def height(self):
        """placeholder for future comments"""
        return self.__height

    @height.setter
    def height(self, height):
        """placeholder for future comments"""
        self.__height = height

    @property
    def x(self):
        """placeholder for future comments"""
        return self.__x

    @x.setter
    def x(self, x):
        """placeholder for future comments"""
        self.__x = x

    @property
    def y(self):
        """placeholder for future comments"""
        return self.__y

    @y.setter
    def y(self, y):
        """placeholder for future comments"""
        self.__y = y

    def __str__(self):
        """string & print functionality"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """find area of rectangle"""
        return self.__width * self.__height
