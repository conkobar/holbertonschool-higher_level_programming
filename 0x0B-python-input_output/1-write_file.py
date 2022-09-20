#!/usr/bin/python3
"""writes to a text file"""


def write_file(filename="", text=""):
    "writes a string to a file"
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
