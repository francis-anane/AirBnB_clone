#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """City class that represents a city within a state.

    Attributes:
        state_id (str): The ID of the state that the city is in.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
