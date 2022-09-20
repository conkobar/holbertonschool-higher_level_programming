#!/usr/bin/python3
"""module for the square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class inheriting from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """defines the size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size

    def __str__(self):
        """string & print functionality"""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x,
            self.y, self.height
        )
