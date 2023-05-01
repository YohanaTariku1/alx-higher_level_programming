#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) == 0 else ""
    payload = {"q": arg}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        r_dict = r.json()
        _id, name = r_dict.get('id'), r_dict.get('name')

        if not len(r_dict) or not _id or not name:
            print("No Result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except:
        print("Not a valid JSON")
