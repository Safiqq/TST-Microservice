# pylint: disable=duplicate-code
"""
This module defines Pydantic models for managing user records in the application.
"""
from pydantic import BaseModel

from app.models.user import UserDB


class User(BaseModel):
    """
    Represents a user record with the following properties:

    * **username**: The username of the user.
    * **password**: The password of the user (hashed and salted).
    """

    username: str
    password: str

    def to_db(self):
        """
        Converts the User object to a UserDB object suitable for database storage.

        Returns:
            A UserDB object containing the information from the User object.
        """
        return UserDB(**self.model_dump())
