#!/usr/bin/python3


"""
functions:
    inherits_from
"""


def inherits_from(obj, a_class):
    """
    this function validate if is a subclass and
    Args:
    obj: any
    a_class: any
    return:True or False
    """
    if obj.__class__ is a_class:
        return False
    return issubclass(obj.__class__, a_class)
