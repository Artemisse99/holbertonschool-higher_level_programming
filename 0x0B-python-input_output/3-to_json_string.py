#!/usr/bin/python3
""" json string function """
import json


def to_json_string(my_obj):
    """ declare function """
    return(json.dumps(my_obj, sort_keys=True))
