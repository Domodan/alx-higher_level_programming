#!/usr/bin/python3
"""
Creates a Square
"""


class Square:
    """
    Members of the square class
    """
    def __init__(self, size=0):
        """
        Instantiation with size

        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of asquare
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        size getter: Handle size errors
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter: Set the size square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
