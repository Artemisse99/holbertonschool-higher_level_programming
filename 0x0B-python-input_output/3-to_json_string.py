#!/usr/bin/python3
import json
""" to json string """


def to_json_string(my_obj):
    """ declare function """
    return(json.dumps(my_obj, sort_keys=True))
