#!/usr/bin/python3
"""

Module: Square

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Square  inherits from Rectangle
        Attributes:
            size (int): side of square
        Methods:
            __init__ - initialises the square
    """
    def __init__(self, size):
        """
        Initializes the values
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        Prints the description of the Rectangle
        """
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string
