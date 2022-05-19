#!/bin/bash
# takes in a URL, sends a GET request to the URL
Curl -s "$1" -X -G -L
