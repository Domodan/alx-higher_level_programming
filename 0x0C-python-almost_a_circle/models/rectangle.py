#!/usr/bin/python3
"""
    Module: Rectangle extends Base class
"""

from models.base import Base


class Rectangle(Base):
    """
        Class: Rectangle extends  Base class

        Methods:
            __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Init Rectangle instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
