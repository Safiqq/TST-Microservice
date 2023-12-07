"""
This module defines Pydantic models for managing location records in the application.
"""
from pydantic import BaseModel

from app.models.model import LocationDB


class Location(BaseModel):
    """
    Represents a location record with the following properties:

    * **type**: The type of the location (e.g., farm, pasture, etc.).
    * **name**: The name of the location.
    * **address**: The address of the location.
    """

    type: str
    name: str
    address: str

    def to_db(self):
        """
        Converts the Location object to a LocationDB object suitable for database storage.

        Returns:
            A LocationDB object containing the information from the Location object.
        """
        return LocationDB(**self.model_dump())
