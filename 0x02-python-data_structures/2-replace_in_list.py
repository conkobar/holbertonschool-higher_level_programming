#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    # replace element of list with new element
    for x in range(len(my_list)):
        if x == idx:
            my_list[x] = element

    return my_list
