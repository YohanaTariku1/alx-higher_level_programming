#!/usr/bin/python3
"""Script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""
import sys
import requests


if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    if r.ok:
        print(r.text)
    else:
        print(f'Error code: {r.status_code}')
