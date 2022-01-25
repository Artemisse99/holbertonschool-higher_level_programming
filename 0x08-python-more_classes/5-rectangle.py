#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:

    """ Instantiation class Rectangle """
    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
    def __del__(self):
        """prints when omegalul is deleted"""
        print("Bye rectangle...")
        
    """ to Make a value private """
    @property
    def width(self):
        return self.__width

    """ get value private """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ to Make a value private """
    @property
    def height(self):
        return self.__height

    """ get value private """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ get area """
    def area(self):
        area = self.width * self.height
        return area

    """ get perimeter """
    def perimeter(self):

        if self.width == 0 | self.height == 0:
            Perimeter = 0
            return Perimeter

        else:
            Perimeter = ((2 * self.width) + (2 * self.height))
            return Perimeter

    """ str # """
    def __str__(self):
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    """ repr """
    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
