#!/usr/bin/python3
"""
    takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""
from sys import argv
import requests


if __name__ == '__main__':
    print(
        requests.get(
            "https://api.github.com/user", auth=(argv[1], argv[2])
        ).json().get('id')
    )
