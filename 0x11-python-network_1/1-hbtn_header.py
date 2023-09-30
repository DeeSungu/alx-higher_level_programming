#!/usr/bin/python3
"""Fetches a URL and prints the value of X-Request-Id found in the response header."""

import sys
import urllib.request

def get_x_request_id(url):
    """Send a request to the URL and return the value of X-Request-Id from the response header."""
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            headers = dict(response.headers)
            return headers.get("X-Request-Id")
    except urllib.error.URLError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)

    if x_request_id is not None:
        print(f"The X-Request-Id is: {x_request_id}")
