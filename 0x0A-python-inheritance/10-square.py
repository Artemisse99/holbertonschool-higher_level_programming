#!/usr/bin/python3
"""class BaseGeometry and subclass Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """empty"""
    def __init__(self, size):
        """empty"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
