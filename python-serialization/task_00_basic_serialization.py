#!/usr/bin/python3

"""00_basic_serialization:
This module allows to serialize a Python dictionary into a JSON file and also
rebuild that object from the JSON file
"""

from json import dump, load


def serialize_and_save_to_file(data, filename):
    with open(filename, mode="w", encoding="utf-8") as f:
        dump(data, f)


def load_and_deserialize(filename):
    with open(filename, encoding="utf-8") as f:
        return load(f)
