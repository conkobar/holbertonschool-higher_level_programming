#!/usr/bin/python3
"""fetches an internet status"""
import urllib.request
import urllib.parse


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        url = response.read()
        print(
            'Body response:',
            f'type: {type(url)}',
            f'content: {str(url)}',
            f'utf8 content: {url.decode()}',
            sep='\n\t- '
        )
