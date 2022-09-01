#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    # print given list in reverse
    my_list.reverse()

    if my_list:
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]), sep="\n")
