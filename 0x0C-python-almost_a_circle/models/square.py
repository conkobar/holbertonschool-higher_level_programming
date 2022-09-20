#!/usr/bin/python3
"""module for the square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class inheriting from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
