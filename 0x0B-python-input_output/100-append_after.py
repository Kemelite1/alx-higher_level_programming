#!/usr/bin/python3
""" a module that executes a function that appends a line """


def append_after(filename="", search_string="", new_string=""):
    """ a function that appends a new line when a string is found

    Args:
        filename: filename
        search_string: string to search
        new_string: string to append

    """

    new_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            new_line += [line]
            if line.find(search_string) != -1:
                new_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(new_line))
