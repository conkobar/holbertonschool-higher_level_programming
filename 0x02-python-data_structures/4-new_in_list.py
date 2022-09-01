#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    # make new list with replacement element @index
    cp = my_list.copy()

    for x in range(len(cp)):
        if x == idx:
            cp[x] = element
            return cp
