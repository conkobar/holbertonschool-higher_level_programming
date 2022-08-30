#!/usr/bin/python3
def print_last_digit(number):

    # string it up
    billy = repr(number)

    # print the string
    print("{}".format(billy[-1]), end="")

    # return it
    return billy[-1]
