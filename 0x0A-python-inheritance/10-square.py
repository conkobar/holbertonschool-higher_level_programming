#!/usr/bin/python3
"""empty class per given task"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """new square class forked from rectangle class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
