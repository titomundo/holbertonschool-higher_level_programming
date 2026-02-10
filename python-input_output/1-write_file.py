#!/usr/bin/python3

"""
1-write_file.py: Writes text to a UTF-8 file with python
"""


def write_file(filename="", text=""):
    """
    read_file: writes text to a utf-8 file
    Args:
        filename (string): name of the file to write to
        text (string): text to write to the file
    """
    with open(filename, mode="w+", encoding="utf-8") as f:
        w = f.write(text)

    return w
