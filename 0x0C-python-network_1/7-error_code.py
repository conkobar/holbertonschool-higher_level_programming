#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL
    and displays the body of the response
"""
from sys import argv
import requests


if __name__ == '__main__':
    content = requests.get(argv[1])
    err = content.status_code
    print(
        "Error code: {}".format(err) if err >= 400 else content.text
    )
