#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class to represent user reviews for Airbnb rentals.

    Attributes:
        place_id (str): The ID of the rental being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
