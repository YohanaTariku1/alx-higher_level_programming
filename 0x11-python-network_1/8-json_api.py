#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == '__main__':
    arg = ""
    if len(sys.argv) == 2:
        arg = sys.argv[1]
    payload = {"q": arg}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    r_dict = r.json()

    if not r.headers.get('Content-Type').startswith('application/json'):
        print("Not a valid JSON")
        sys.exit()

    if len(r_dict) == 0:
        print("No Result")
        sys.exit()
    print(f"[{r_dict.get('id')}] {r_dict.get('name')}")
