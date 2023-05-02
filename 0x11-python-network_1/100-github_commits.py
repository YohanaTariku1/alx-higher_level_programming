#!/usr/bin/python3
"""Script that takes 2 arguments:
    The first argument will be the repository name
    The second argument will be the owner name

"""
from sys import argv
import requests


if __name__ == '__main__':
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    payload = {"Accept": "application/vnd.github+json"}
    r = requests.get(url, params=payload)

    response_list = r.json()
    for idx, val in enumerate(response_list):
        if idx >= 10:
            break
        print(f"{val.get('sha')}: \
        {val.get('commit').get('author').get('name')}")
