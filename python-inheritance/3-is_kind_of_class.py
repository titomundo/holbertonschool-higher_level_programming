#!/usr/bin/python3

"""
3-is_kind_of_class: checks if an instance is a specific class
or inherited from that class
"""


def is_kind_of_class(obj, a_class):
    """is_same_class:
    returns true if an instance obj is of the
    type a_class or inherited from a_class
    Args:
        obj (instance): object to inspect
        a_class (class): class name to compare to obj"""

    if obj.__class__ is a_class or obj.__class__ in a_class.__subclasses__():
        return True
    else:
        return False
