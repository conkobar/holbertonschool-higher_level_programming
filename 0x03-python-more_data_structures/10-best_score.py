#!/usr/bin/python3


# returns largest value of keys
def best_score(a_dictionary):
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
