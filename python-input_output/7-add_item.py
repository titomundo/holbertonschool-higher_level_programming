#!/usr/bin/python3

"""7-add_item:
Adds the program arguments to a JSON representation file
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
obj = []

try:
    obj = load_from_json_file(filename)
except Exception as Err:
    pass

args = sys.argv
obj.extend(args[1:])
save_to_json_file(obj, filename)
