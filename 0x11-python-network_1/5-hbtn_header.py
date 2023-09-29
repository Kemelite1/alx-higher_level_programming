#!/usr/bin/python3
import requests
import sys

"""
Displays the X-Request-Id header variable of a request to
a given URL
"""
if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
