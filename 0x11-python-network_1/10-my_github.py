#!/usr/bin/python3
"""script that takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id
"""
from sys import argv
from requests.auth import HTTPBasicAuth
import requests


if __name__ == '__main__':
    url = f"https://api.github.com/users/"
    r = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2])) 

    print(r.json().get('id'))
