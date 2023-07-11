#!/usr/bin/python3
""" this is a module that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ a function that creates an Object from a JSON file

    Args:
        filename: textfile name

    Raises:
        Exception: when the object can't be encoded

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
