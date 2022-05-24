#!/usr/bin/python3
"""script that takes your GitHub credentials
   (username and password) and uses the GitHub
   API to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    req = requests.Session()
    req.auth = (argv[1], argv[2])
    eq = req.get(url)
    try:
        print('{}'.format(eq.json()['id']))
    except:
        print("None")
