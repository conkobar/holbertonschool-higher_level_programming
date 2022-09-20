#!/usr/bin/python3
"""module for task 10"""


class Student:
    """defines student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs:
            jays = {}
            for key, value in vars(self).items():
                if key in attrs:
                    jays[key] = value
            return jays

        return vars(self)
