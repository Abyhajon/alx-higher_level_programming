#!/usr/bin/python3
"""Takes my Github creds (username & password)
and uses the Github API to display my ID
"""

from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    r = requests.get(url,
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
