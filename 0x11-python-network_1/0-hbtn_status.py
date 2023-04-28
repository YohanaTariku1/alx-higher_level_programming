#!/usr/bin/python3
"""Fetches 'https://alx-intranet.hbtn.io/status'"""
import urllib.parse
import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    html = response.read()
    print("Body response:")
    print(f"    - type: {type(html)}")
    print(f"    - content: {html}")
    print(f"    - utf8: {html.decode('utf-8')}")
