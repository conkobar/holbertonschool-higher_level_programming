#!/usr/bin/python3
'''This module sends a POST with a letter as a parameter'''
import requests
import sys


if __name__ == '__main__':
    pack = {}
    if len(sys.argv) >= 2:
        pack['q'] = sys.argv[1]
    else:
        pack['q'] = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data=pack)
    try:
        res = req.json()
        if res == {}:
            print('No result')
        else:
            print('[{}] {}'.format(res['id'], res['name']))
    except Exception:
        print('Not a valid JSON')
