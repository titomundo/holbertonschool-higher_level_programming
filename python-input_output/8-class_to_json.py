#!/usr/bin/python3

"""8-class_to_json:
Return the dictionary description of a class for a JSON object
"""


def class_to_json(obj):
    return obj.__dict__
