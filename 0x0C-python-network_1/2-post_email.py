#!/usr/bin/python3
"""
    takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
from sys import argv
from urllib import request, parse


if __name__ == '__main__':
    content = parse.urlencode({'email': argv[2]})
    content = content.encode()
    email = request.Request(argv[1], content)
    with request.urlopen(email) as res:
        print(res.read().decode('utf8'))
