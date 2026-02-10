#!/usr/bin/python3

"""
0-read_file.py: Print lines from a UTF-8 file in python
"""


def read_file(filename=""):
    """
    read_file: prits the content of a utf-8 file
    Args:
        filename (string): name of the file to read
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
