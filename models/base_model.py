#!/usr/bin/python3

"""base_model for the AirBnB_clone"""

import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for the AirBnB_clone objects
    """

    def __init__(self, *args, **kwargs):
        """Constructor for BaseModel
        Args:
            args: tuple of arguments to Basemodel to create a new object
            kwargs: key/value arguments to Basemodel to create a new object
        Attributes:
            id: Unique identity for objects
            created_at: The time an object was created
            updated_at: The time an object was updated
        """

        # Create a BaseModel object with the key/value arguments to BaseModel
        try:
            if len(kwargs) != 0:
                for key in kwargs:
                    if key == "id":
                        self.__dict__["id"] = kwargs["id"]
                    elif key == "created_at":
                        self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    elif key == "updated_at":
                        self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

            else:
                # Create an object with new id and timestamp
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
        except TypeError:
            pass  # for now

    def __str__(self):
        """Return string representation of the class"""

        return f"{[type(self).__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        """Save object updates"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of object"""

        obj_dict = {}  # holds dictionary representation of object
        obj_dict.update(self.__dict__)

        # convert datetime objects to string string (created_at and updated_at)
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        # add object's class name to dictionary
        obj_dict.update({"__class__": type(self).__name__})

        return obj_dict
