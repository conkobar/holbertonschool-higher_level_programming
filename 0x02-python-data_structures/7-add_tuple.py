#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # add two tuples values'
    newt1 = (0, 0)
    newt2 = (0, 0)

    # check len & value of t_a
    if len(tuple_a) == 1:
        newt1 = (tuple_a[0], 0)
    elif len(tuple_a) >= 2:
        newt1 = (tuple_a[0], tuple_a[1])

    # check len & value of t_b
    if len(tuple_b) == 1:
        newt2 = (tuple_b[0], 0)
    elif len(tuple_b) >= 2:
        newt2 = (tuple_b[0], tuple_b[1])

    # return new tuple
    return (newt1[0] + newt2[0], newt1[1] + newt2[1])
