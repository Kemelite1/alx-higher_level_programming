#!/usr/bin/python3
""" a module that returns the dictionary description with a simple
data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """ a function that retuns the dictionary description of an obj """

    test = {}
    if hasattr(obj, "__dict__"):
        test = obj.__dict__.copy()
    return test
