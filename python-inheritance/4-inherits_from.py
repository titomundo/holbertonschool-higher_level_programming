#!/usr/bin/python3

"""
4-inherits_from: checks if an
instance is from an inherited class
"""


def inherits_from(obj, a_class):
    """inherits_from:
    returns true if an instance obj is inherited from a_class
    Args:
        obj (instance): object to inspect
        a_class (class): class name to compare to obj"""
    
    c = obj.__class__

    if not c is a_class and issubclass(c, a_class):
        return True
    else:
        return False
