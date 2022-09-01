#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    # replace element of list with new element
    if idx < 0 and idx >= len(my_list):
        return None

    my_list[idx] = element
    return my_list
