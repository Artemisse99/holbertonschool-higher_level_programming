#!/usr/bin/python3
"""
script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}
    req = requests.post(url, data=payload)

    try:
        dic = req.json()
        if dic:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError as res:
        print("Not a valid JSON")
