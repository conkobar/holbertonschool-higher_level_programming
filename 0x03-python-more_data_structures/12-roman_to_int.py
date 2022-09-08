#!/usr/bin/python3


def roman_to_int(roman_string):
    """ convert string of roman numerals to int """
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0

    if type(roman_string) == str:
        last = 0
        for i in roman_string:
            if last != 0 and last < values[i]:
                sum -= last
            else:
                sum += last
            last = values[i]
        sum += last

    return sum
