#!/usr/bin/python3
"""adds args to python list and save to file"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    jputs = load_from_json_file("add_item.json")
except:
    jputs = []

save_to_json_file(jputs + argv[1:], "add_item.json")
