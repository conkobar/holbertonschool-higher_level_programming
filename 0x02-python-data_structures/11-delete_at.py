#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    # deletes item at index
    if idx > 0 and idx < len(my_list):
        del(my_list[idx])

    # return list if it exists
    return my_list if my_list else None
