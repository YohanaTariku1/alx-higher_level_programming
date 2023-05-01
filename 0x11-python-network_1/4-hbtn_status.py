#!/usr/bin/python3
"""Script that fetches 'https://alx-intranet.hbtn.io/status'"""
import requests

response = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print(f'\t- type: {type(response.text)}')
print(f'\t- content: {response.text}')
