#!/usr/bin/python3


# replaces or adds key/value to dict
def update_dictionary(a_dictionary, key, value):
    if key and value:
        a_dictionary[key] = value
    return a_dictionary
