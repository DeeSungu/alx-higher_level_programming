#!/usr/bin/python3
""" A Py script that fetches https://alx-intranet.hbtn.io/status
import urllib.request"""

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(f"Body response:\n{''.join(['\t' + line for line in body.splitlines(True)])}")
except urllib.error.URLError as e:
    print(f"Error fetching the URL: {e}")

