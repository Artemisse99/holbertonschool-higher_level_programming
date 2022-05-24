#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to
    the passed URL with the email as a parameter
"""
from urllib.request import urlopen
from urllib import parse
import urllib.request
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    fields = {"email": argv[2]}

    data = urllib.parse.urlencode(fields)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
