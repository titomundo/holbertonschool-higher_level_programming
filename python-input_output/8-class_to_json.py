#!/usr/bin/python3

"""8-class_to_json:
Return the dictionary description of a class for a JSON object
"""


def class_to_json(obj):
    """class_to_json:
    returns a dictionary for a json object
    """
    return obj.__dict__
