#!/usr/bin/python3


# print dict by ordered keys
def print_sorted_dictionary(a_dictionary):
    # itereate thru dict
    for node in sorted(a_dictionary):
        print("{}: {}".format(node, a_dictionary[node]))
