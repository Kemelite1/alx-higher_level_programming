#!/usr/bin/python3
import requests
import sys
from requests.auth import HTTPBasicAuth

"""
Takes your Github credentials(username and password)
uses the Github API to display your Id
"""

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
