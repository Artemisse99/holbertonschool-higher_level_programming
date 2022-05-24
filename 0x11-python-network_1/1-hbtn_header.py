#!/usr/bin/python3
"""Write a Python script that fetches
https://intranet.hbtn.io/status"""
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        info = response.getheader("X-Request-Id")
        print(info)
