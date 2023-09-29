#!/usr/bin/python3

"""
Takes your Github credentials(username and password)
uses the Github API to display your Id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
