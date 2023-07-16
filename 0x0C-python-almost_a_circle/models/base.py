#!/usr/bin/python3
''' a base model class'''
import csv
import json

class Base:
    ''''represents the base of all classes created'''

    __nb_objects = 0


    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
