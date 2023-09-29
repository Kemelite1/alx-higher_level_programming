#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys
"""
Takes in a URL, sends a POST request to the passed URL,
takes email as a parameter and displays the body of the
response
"""

if __name__=='__main__':
    url = sys.argv[1]
    parameters = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
