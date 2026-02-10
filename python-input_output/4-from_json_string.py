#!/usr/bin/python3

"""
4-from_json_string: Return an object from a json string representation
"""
from json import loads


def from_json_string(my_str):
    """
    from_json_string: returns an object from a json string representation
    Args:
        my_str (str): json to convert to object
    """
    return loads(my_str)
