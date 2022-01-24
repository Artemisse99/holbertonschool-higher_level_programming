""" Class Rectangle """
class Rectangle:

    """ Instantiation class Rectangle """
    def __init__(self, width=0, height=0):

        self.width = width
        self.height= height

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
