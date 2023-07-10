#!/usr/bin/python3
"""
    Module: MyInt - Inherits from int class
"""


class MyInt(int):
    """

    Inherits from int class

    """
    def __init__(self, value):
        """

        Initialize value

        """
        self.value = value

    def __ne__(self, x):
        """

        Not equal to comparison

        """
        if self.value is x:
            return True

    def __eq__(self, x):
        """

        Equal to comparison
        
        """
        return not self.__ne__(x)
