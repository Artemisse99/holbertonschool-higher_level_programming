#!/bin/bash
# takes in a URL, sends a GET request to the URL
Curl -G "$1" -L
