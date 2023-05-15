#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class for managing user objects.

    This class inherits from the BaseModel class and includes attributes
    for email, password, first name, and last name. These attributes represent
    the data associated with a user object.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
