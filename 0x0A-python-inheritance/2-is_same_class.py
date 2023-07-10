#!/usr/bin/python3
"""returns True if the object is exactly an instance of the specified class
if not then  False.
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance"""
    return(isinstance(obj, a_class))
