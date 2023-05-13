#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines the Amenity class that inherits from the BaseModel class.

    Attributes:
        name (str): The name of the Amenity.
    """
    name = ""
