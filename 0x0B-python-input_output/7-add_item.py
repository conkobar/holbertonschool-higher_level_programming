#!/usr/bin/python3
"""adds args to python list and save to file"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


jputs = load_from_json_file(add_item.json)
jputs += sys.argv[1:]
save_to_json_file(jputs, "add_item.json")
