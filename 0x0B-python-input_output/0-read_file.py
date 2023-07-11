#!/usr/bin/python3
"""
contains a function that reads a text file
"""

def read_file(filename=""):
    """
    a function that reads from a file

    Args:
        filename: filename

    Raises:
        Exception: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end="")
