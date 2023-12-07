"""
This module defines Pydantic models for managing livestock records in the application.
"""
from datetime import date
from pydantic import BaseModel
from app.models.model import LivestockDB


class Livestock(BaseModel):
    """
    Represents a livestock record with the following properties:

    * **name**: The name of the livestock.
    * **breed**: The breed of the livestock.
    * **species**: The species of the livestock.
    * **birthplace_id**: The ID of the location where the livestock was born.
    * **birthdate**: The date of birth of the livestock.
    * **gender**: The gender of the livestock.
    * **location_id**: The ID of the current location of the livestock.
    """

    name: str
    breed: str
    species: str
    birthplace_id: int
    birthdate: date
    gender: str
    location_id: int

    def to_db(self):
        """
        Converts the Livestock object to a LivestockDB object suitable for database storage.

        Returns:
            A LivestockDB object containing the information from the Livestock object.
        """
        return LivestockDB(**self.model_dump())
