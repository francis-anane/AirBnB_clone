#!/usr/bin/python3

"""base_model for the AirBnB_clone"""

import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for the AirBnB_clone objects
    Attributes:
    __nb_objects (int): Keeps track of base objects count
    """

    def __init__(self, id, created_at, updated_at):
        """Constructor for BaseModel
        Args:
            id: Unique identity for objects
            created_at: The time an object was created
            updated_at: The time an object was updated
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Return string representation of the class"""

        return f"{[type(self).__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        """Save object updates"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of object"""

        if type(self.created_at) is not str:
            self.created_at = self.created_at.isoformat()
        if type(self.updated_at) is not str:
            self.updated_at = self.updated_at.isoformat()
        obj_dict = self.__dict__  # holds dictionary representation object
        obj_dict.update({"__class__": type(self).__name__})

        return obj_dict
