#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    # completes squares of all ints in matrix
    # create empty matrix
    dupe = [[]]

    # append squares to new matrix
    for idx in matrix:
        dupe.append(list(map(lambda x: x ** 2, i)))

    # return new matrix
    return dupe
