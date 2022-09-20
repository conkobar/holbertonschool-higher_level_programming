#!/usr/bin/python3
"""adds args to python list and save to file"""
import sys
import json
save = __import__('5-save_to_json_file').save_to_json_file
lode = __import__('6-load_from_json_file').load_from_json_file


jputs = lode(add_item.json)
jputs += sys.argv[1:]
save(jputs, "add_item.json")
