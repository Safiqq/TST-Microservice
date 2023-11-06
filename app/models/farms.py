"""
This module defines the Farm data model using Pydantic.
The Farm class represents the attributes and structure of a farm, including its name, location,
number of barns, total capacity, owner name, and phone number.
"""

from pydantic import BaseModel


class Farm(BaseModel):
    """
    Farm Model

    Represents a farm with various attributes.

    Attributes:
        id (int): The unique identifier for the farm.
        farm_name (str): The name of the farm.
        farm_location (str): The location address of the farm.
        number_of_barns (int): The number of barns on the farm.
        total_capacity (int): The total capacity of the farm.
        owner_name (str): The name of the farm owner.
        phone_number (str): The phone number of the farm owner.

    Config:
        json_schema_extra (dict): An example JSON object representing a farm.
    """

    id: int = None
    farm_name: str
    farm_location: str
    number_of_barns: int
    total_capacity: int
    owner_name: str
    phone_number: str

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Farm Model Configuration

        This class provides additional configuration options for the Farm model.

        Attributes:
            json_schema_extra (dict): A JSON object representing an example farm.
        """

        json_schema_extra = {
            "example": {
                "farm_name": "Peternakan XYZ",
                "farm_location": "Jl. Peternakan No. 456",
                "number_of_barns": 6,
                "total_capacity": 1500,
                "owner_name": "Jane Smith",
                "phone_number": "081234567891",
            },
        }
