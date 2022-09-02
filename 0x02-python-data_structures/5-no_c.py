#!/usr/bin/python3


def no_c(my_string):
    # replace c & C in given string
    return my_string.translate({ord(c): None for c in 'cC'})
