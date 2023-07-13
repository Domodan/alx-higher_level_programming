#!/usr/bin/python3
"""
    Module: Base Class
"""


class Base:
    """
        The base model

        Attributes:
            __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize Base Class Objects

            Args:
                id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
