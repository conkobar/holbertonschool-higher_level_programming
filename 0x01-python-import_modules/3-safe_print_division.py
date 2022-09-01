#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        # test expected error
        tot = a / b

    except ZeroDivisionError:
        # handle the error
        tot = None

    finally:
        # always gets executed, regardless
        print("Inside redult: {}".format(tot))
        return tot
