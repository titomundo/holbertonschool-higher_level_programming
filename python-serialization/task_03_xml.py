#!/usr/bin/python3

"""task_03_xml:
Converting XML files to JSON in Python
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Reads a dictionary and writes the entries to a XML file

    Args:
        dictionary (dict) dictionary to convert
        filename (string) name of the file to write into
    """
    root = ET.Element("data")
    tree = ET.ElementTree(root)

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    ET.indent(tree)
    tree.write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """Parses a XML file and converts the contents to a dictionary

    Args:
        filename (str): name of the file to parse

    Returns: Python dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    d = {}

    for child in root:
        d.update({child.tag: child.text})

    return d
