#!/usr/bin/python3

"""
Takes in a letter, sends POST request to
http://0.0.0.0:5000/search_user with the letter as 
a parameter
"""
import requests
import sys
if __name__ == "__main__":
    try:
        param = {"q": sys.argv[1]}
    except IndexError:
        param = {"q": ""}
    response = requests.post("http://0.0.0.0:5000/search_user", data=param)
    res = response.json()
    try:
        if res:
            print("[{}] {}".format(res.get("id"), res.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
