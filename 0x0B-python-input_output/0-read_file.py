#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """Read file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
