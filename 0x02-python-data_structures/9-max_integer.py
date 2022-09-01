#!/usr/bin/python3


def max_integer(my_list=[]):
    # find the biggest int in list
    big = 0
    for i in my_list:
        if i > big:
            big = i
            continue

        return big if i else None
