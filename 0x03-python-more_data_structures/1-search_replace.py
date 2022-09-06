#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    replace occurrences of @search
    in @my_list with @ replace
    """
    new_list = []

    for node in my_list:
        if node == search:
            new_list.append(replace)
        else:
            new_list.append(node)

    return new_list
