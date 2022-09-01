#!/usr/bin/python3


def multiple_returns(sentence):
    # returns tuple with the length
    # of a string and its first char

    first = (sentence[0] if sentence else None)
    length = len(sentence)

    return (length, first)
