#!/usr/bin/python3
"""new class inherited from list"""


class MyList(list):
    """new list type object"""
    def print_sorted(self):
        print(sorted(self))
