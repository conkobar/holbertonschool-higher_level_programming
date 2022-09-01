#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    # finds all multiples of 2 in list
    if my_list:
        new = []
        for i in my_list:
            if i % 2 == 0:
                switch = True
            else:
                switch = False
            new.append(switch)

    else:
        new = None

    return new
