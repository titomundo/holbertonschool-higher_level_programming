#!/usr/bin/python3

"""
2-append_write: Appends text to a UTF-8 file with python
"""


def append_write(filename="", text=""):
    """
    append_write: appends text to a utf-8 file
    Args:
        filename (string): name of the file to write to
        text (string): text to write to the file
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        w = f.write(text)

    return w
