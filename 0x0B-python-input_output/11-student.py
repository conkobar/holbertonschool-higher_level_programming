#!/usr/bin/python3
"""module for task 10"""


class Student:
    """defines student class for task 10"""
    def __init__(self, first_name, last_name, age):
        """maybe this is what it wants all of a sudden"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        """comments go here i guess"""
        if attrs is not None:
            jays = {}
            for key, value in vars(self).items():
                if key in attrs:
                    jays[key] = value
            return jays

        return vars(self)


    def reload_from_json(self, json):
        """loads student info from dict"""
        for key, value in json.items():
            setattr(self, key, value)
