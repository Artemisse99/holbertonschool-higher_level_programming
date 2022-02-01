#!/usr/bin/python3
"""Creates Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """empty"""
    def __init__(self, width, height):
        """empty"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        
    def area(self):
        """empty"""
        return self.__width * self.__height
    
    def __str__(self):
        """empty"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
