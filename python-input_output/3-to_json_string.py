#!/usr/bin/python3

from json import dumps
"""
2-to_json_string: Return the json string representation of a python object
"""


def to_json_string(my_obj):
    """
    to_json_string: returns an object as a json representation
    Args:
        my_obj (object): object to convert to json
    """
    return dumps(my_obj)
