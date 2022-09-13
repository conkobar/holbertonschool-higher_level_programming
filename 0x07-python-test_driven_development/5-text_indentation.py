#!/usr/bin/python3
""" function appends newlines to some punctuation """


def text_indentation(text):
    """ makes a string really weird """
    if type(text) == str:
        text = text.replace(".", ".\n\n")
        text = text.replace("?", "?\n\n")
        text = text.replace(":", ":\n\n")
        print(text)
    else:
        raise TypeError("text must be a string")
