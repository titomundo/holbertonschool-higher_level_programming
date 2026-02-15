#!/usr/bin/python3

"""task_02_csv:
Converting Comma Separated Values to JSON in python
"""

from csv import DictReader
from json import dump


def convert_csv_to_json(filename):
    """Reads a csv file and dumps the data into a json file

    Args:
        filename (str): name of the csv file to read
    """
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as csvf:
            data = list(DictReader(csvf))

        with open("data.json", mode="w", encoding="utf-8") as jsonf:
            dump(data, jsonf, indent=4)

        return True

    except Exception:
        return False
