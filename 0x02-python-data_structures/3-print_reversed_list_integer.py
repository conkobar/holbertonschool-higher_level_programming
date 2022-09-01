#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    # print given list in reverse
    my_list.reverse()
    l_length = len(my_list)

    if l_length > 0:
        for i in range(l_length):
            print("{:d}".format(my_list[i]), sep="\n")
