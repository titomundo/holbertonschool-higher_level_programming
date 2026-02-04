#!/usr/bin/python3

"""0-lookup: gets attributes and methods of an object"""


def lookup(obj):
    """returns a list with the attributes and methods of an object
    Args:
        obj (object): object to inspect
    Returns: list"""

    return dir(obj)
