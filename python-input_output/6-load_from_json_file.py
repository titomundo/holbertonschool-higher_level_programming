#!/usr/bin/python3

"""6-load_from_json_file: Create a python object from a JSON file"""

from json import load


def load_from_json_file(filename):
    """load_from_json_file: returns an object built from a json file

    Args:
        filename (str): name of the file to read from
    """
    with open(filename, encoding="utf-8") as f:
        return load(f)
