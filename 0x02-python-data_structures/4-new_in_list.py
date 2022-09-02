#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    # make new list with replacement element @index
    if my_list:
        cp = my_list.copy()
        for x in range(len(cp)):
            if x == idx:
                cp[x] = element
                break
    else:
        cp = None

    return cp
