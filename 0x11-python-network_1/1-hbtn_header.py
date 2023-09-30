#!/usr/bin/python3
"""Python script that fetches a URL and prints the value of the X-request-id found in the response header"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
