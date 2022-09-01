#!/usr/bin/python3


def max_integer(my_list=[]):
    # find the biggest int in list
    if my_list:
        big = 0
        for i in my_list:
            if i > big:
                big = i
                continue

    # null if given null
    else:
        big = None

    # return the biggest int
    return big
