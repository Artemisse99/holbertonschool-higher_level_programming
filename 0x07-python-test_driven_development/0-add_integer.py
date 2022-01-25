#!/usr/bin/python3
"""
Adding module
This module supplies with one function, add_integer(a, b)
"""
def add_integer(a, b=98):
    """Return add of a + b"""
    if not isinstance(a, (int, float)):
       raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
       raise TypeError("b must be an integer")
    return a + b
