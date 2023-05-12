#!/usr/bin/python3

""" file_storage module """

import json


class FileStorage:
    """ serializes objects to a JSON file and deserializes JSON file to objects

    Attributes:
        __file_path (str): Path to the JSON file
        __objects (dict): Stores all objects by class_name.id in a dictionary
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects"""

        return self.__objects

    def new(self, obj):
        """Add new object to the dictionary (__objects)
        Args:
            obj: class_name.id to add to __objects
        """

        self.__objects.update({f"{type(obj).__name__}.{obj.id}":obj.to_dict()})

    def save(self):
        """ Serializes __objectts to the JSON file __file_path"""

        with open(self.__file_path, "a") as a_file:
            json.dump(self.__objects, a_file)

    def reload(self):
        """Deserializes the JSON file __file_path to __objects"""

        try:
            with open(self.__file_path, "r") as a_file:
                self.__objects = json.load(a_file)
        except FileNotFoundError:
            pass  # pass for now
