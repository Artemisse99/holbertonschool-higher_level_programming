#!/usr/bin/python3
""" Write a Python script that fetches
    https://intranet.hbtn.io/status
"""

from urllib.request import urlopen

if __name__ == "__main__":

    with urlopen("https://intranet.hbtn.io/status") as res:
        body = res.read()
        print('Body response:')
        print('\t''- type: ' + str(type(body)))
        print('\t''- content: ' + str(body))
        print('\t' + '- utf8 content: ' + body.decode("utf-8"))
