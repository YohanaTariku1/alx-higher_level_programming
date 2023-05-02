#!/usr/bin/python3
"""script that takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id
"""
from sys import argv
import requests


if __name__ == '__main__':
    url = f"https://api.github.com/users/{argv[1]}"
    payload = {"Authorization": f"Bearer {argv[2]},\
            Accept: application/vnd.github+json"}
    r = requests.get(url, params=payload)

    print(r.json()['id'])
