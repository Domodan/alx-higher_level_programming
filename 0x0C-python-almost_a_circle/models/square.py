#!/usr/bin/python3
"""
    Module: Square class from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square class implements rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes the instance of the class

            Args:
                size: size of the square
                x: x coordinate of the square
                y: y coordinate of the square
                id: id of the square
        """
        super().__init__(size, size, x, y, id)
