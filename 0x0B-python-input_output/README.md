This directory contains tasks on file input and output in python. How to open a file, write text in a file, read a file line by line etc.

|Task                                                                         |    prototype
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
|Task 0
|Write a function that reads a text file (UTF8) and prints it to stdout You must use the with statement | def read_file(filename=""):
|Task 1
|Write a function that writes a string to a text file (UTF8) and returns the number of characters written Your function should create the file if doesn’t exist and overwite the content if it a|already exists |def write_file(filename="", text=""):
|task 2
|Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added and if the file does not exist the create it |def append_write(filename="", text=""):
|task 3
|Write a function that returns the JSON representation of an object (string). You don’t need to manage exceptions if the object can’t be serialized. |def to_json_string(my_obj):
|task 4
|Write a function that returns an object (Python data structure) represented by a JSON string. You don’t need to manage exceptions if the JSON string doesn’t represent an object. |def from_json_string(my_str):
|task 5
|Write a function that writes an Object to a text file, using a JSON representation:You don’t need to manage exceptions if the object can’t be serialized.You don’t need to manage file permission exceptions. | def save_to_json_file(my_obj, filename):
|task 6
|Write a function that creates an Object from a “JSON file”:You don’t need to manage exceptions if the JSON string doesn’t represent an object.You don’t need to manage file permissions / exceptions. | def load_from_json_file(filename):
|task 7
|Write a script that adds all arguments to a Python list, and then save them to a file:You must use your function save_to_json_file from 5-save_to_json_file.py.You must use your function load_from_json_file from 6-load_from_json_file.pyThe list must be saved as a JSON representation in a file named add_item.json. If the file doesn’t exist, it should be created 
|task 8
|Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:obj is an instance of a Class. All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean |def class_to_json(obj):
|task 9
|Write a class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
You are not allowed to import any module

task 10
Write a class Student that defines a student by: (based on 9-student.py)
Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attribute names contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module

task 11
Write a class Student that defines a student by: (based on 10-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attributes name contain in this list must be retrieved.
Otherwise, all attributes must be retrieved
Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
You can assume json will always be a dictionary
A dictionary key will be the public attribute name
A dictionary value will be the value of the public attribute
You are not allowed to import any module
Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)

task 12
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module
