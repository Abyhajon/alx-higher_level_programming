#!/usr/bin/python3

"""
display the error message or the body of the response decoded in utf-8
the error code should be returned
"""

import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
