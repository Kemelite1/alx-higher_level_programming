#!/usr/bin/python3
import requests
import sys

"""
Takes in a letter, sends POST request to
http://0.0.0.0:5000/search_user with the letter as 
a parameter
"""

if __name__ == "__main__":
    try:
        param = {"q": sys.argv[1]}
    except IndexError:
        param = {"q": ""}
    response = requests.post("http://0.0.0.0:5000/search_user", data=param)
    res = response.json()
    try:
        if res:
            print("[{}] {}".format(res["id"], res["name"]))
        else:
            print("No result")
    except requests.JSONDecodeError:
        print("Not a valid JSON")
