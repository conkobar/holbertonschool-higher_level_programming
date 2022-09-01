#!/usr/bin/python3


def replace_in_list(my_list, idx, element):

    tmp = my_list

    if idx < 0 and idx >= len(my_list):
        return None

    tmp[idx] = element
    return tmp
