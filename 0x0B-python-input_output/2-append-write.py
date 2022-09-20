#!/usr/bin/python3
"""writes into a file"""


def append_write(filename="", text=""):
    """appends string to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
