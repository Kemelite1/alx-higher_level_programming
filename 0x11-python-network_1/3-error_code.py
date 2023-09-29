#!/usr/bin/python3
import sys
from urllib import request, error

"""
Takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
