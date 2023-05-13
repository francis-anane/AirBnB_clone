#!/usr/bin/python3

from models.base_model import BaseModel


class State(BaseModel):
    """A class representing a state object.

    This class inherits from the BaseModel class defined in another module.
    It has a single attribute, `name`, which represents the name of the state.
    """

    name = ""
