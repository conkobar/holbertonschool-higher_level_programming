#!/usr/bin/python3
"""fetches an internet status"""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse


    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        url = response.read()
        print(
            'Body response:',
            f'type: {type(url)}',
            f'content: {str(url)}',
            f'utf8 content: {url.decode()}',
            sep='\n\t- '
        )
