#!/usr/bin/python3


# returns new dict with doubled values
def multiply_by_2(a_dictionary):
    # new dict
    new_dict = a_dictionary.copy()

    # iterate thru and multiply nodes
    for key in new_dict:
        new_dict[key] *= 2

    # return newly factored list
    return new_dict
