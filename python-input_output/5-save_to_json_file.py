#!/usr/bin/python3

"""
5-save_to_json_file: Saves a python object to a text file using JSON format
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file: writes an object to a text file in json representation
    Args:
        my_obj (object): object to write to file
        filename (str): name of the file to write to
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        dump(my_obj, f)
