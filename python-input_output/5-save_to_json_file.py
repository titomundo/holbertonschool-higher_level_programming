#!/usr/bin/python3

"""
5-save_to_json_file: Saves a python object to a text file using JSON format
"""
from json import dump


def save_to_json_file(my_obj, filename):
    with open(filename, mode="w", encoding="utf-8") as f:
        dump(my_obj, f)
