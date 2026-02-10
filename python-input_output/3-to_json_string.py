#!/usr/bin/python3

"""
3-to_json_string: Return the json string representation of a python object
"""
from json import dumps


def to_json_string(my_obj):
    """
    to_json_string: returns an object as a json representation
    Args:
        my_obj (object): object to convert to json
    """
    return dumps(my_obj)
