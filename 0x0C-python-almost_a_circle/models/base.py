#!/usr/bin/python3
"""
    Module: Base Class
"""

import json


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


    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        """
            Write the JSON serialization of a list of objects to a file.

            Args:
                list_objs (list): A list of inherited Base instances.
        """

        filename = cls.__name__ + ".json"

        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))


    @staticmethod
    def from_json_string(json_string):
        """
            Returns list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
