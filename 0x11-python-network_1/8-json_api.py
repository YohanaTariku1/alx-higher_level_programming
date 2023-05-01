#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) == 2 else ""
    payload = {"q": arg}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    if r.headers.get('Content-Type') == 'application/json':
        r_dict = r.json()

        if len(r_dict) == 0:
            print('No result')
        else:
            _id, name = r_dict.get('id'), r_dict.get('name')
            print(f'[{_id}] {name}')
    else:
        print('Not a valid JSON')
