#!/usr/bin/python3

"""2-is_same_class: checks if an instance is a specific class"""


def is_same_class(obj, a_class):
    """is_same_class:
    returns true if an instance obj is of the type a_class
    Args:
        obj (instance): object to inspect
        a_class (class): class name to compare to obj"""

    if obj.__class__ is a_class:
        return True
    else:
        return False
