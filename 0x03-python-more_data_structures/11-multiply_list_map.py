#!/usr/bin/python3


# multplies all nodes by value w/o any loops
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
