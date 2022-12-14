#!/usr/bin/python3
""" project 1151 task 1 """


def matrix_divided(matrix, div):
    """ divides all elements in a matrix by div """
    int_err = "matrix must be a matrix (list of lists) of integers/floats"
    size_err = "Each row of the matrix must have the same size"

    if div <= 0:
        raise ZeroDivisionError("")
    if matrix:
        for n in matrix:
            count = 0
            for i in n:
                if type(i) is float:
                    int(i)
                if type(i) is not int:
                    raise TypeError(int_err)
                count += 1
            if count != len(n):
                raise TypeError(size_err)
        return [[round(i / div, 2) for i in n] for n in matrix]
