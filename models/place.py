#!/usr/bin/python3

from models.base_model import BaseModel


class Place(BaseModel):
    """
    A class to represent a place object with various attributes.

    Attributes:
    - city_id (str): the ID of the city where the place is located.
    - user_id (str): the ID of the user who owns the place.
    - name (str): the name of the place.
    - description (str): a description of the place.
    - number_rooms (int): the number of rooms in the place.
    - number_bathrooms (int): the number of bathrooms in the place.
    - max_guest (int): the maximum number of guests allowed in the place.
    - price_by_night (int): the price per night to stay at the place.
    - latitude (float): the latitude coordinate of the place.
    - longitude (float): the longitude coordinate of the place.
    - amenity_ids (list): a list of IDs for amenities available at the place.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
