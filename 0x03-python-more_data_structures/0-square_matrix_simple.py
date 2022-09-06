#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    # completes squares of all ints in matrix
    # create copy of matrix
    dupe = [[]]

    # append squares to new matrix
    for idx in matrix:
        temp = []
        for i in idx:
            temp.append(i ** 2)
        dupe.append(temp)

    # remove empty element
    if dupe[1]:
        del(dupe[0])

    # return new matrix
    return dupe
