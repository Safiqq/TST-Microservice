"""
This module defines the Duck data model using Pydantic.
The Duck class represents the attributes and structure of a duck, which includes its name, type,
birthplace, birthdate, gender, health status, and the farm it belongs to.
"""

from datetime import date
from pydantic import BaseModel


class Duck(BaseModel):
    """
    Duck Model

    Represents a duck with various attributes.

    Attributes:
        id (int): The unique identifier for the duck.
        duck_name (str): The name of the duck.
        duck_type (str): The type or breed of the duck.
        birthplace (str): The place where the duck was born.
        birthdate (date): The date of birth of the duck.
        gender (str): The gender of the duck (e.g., "Male" or "Female").
        health_status (str): The health status of the duck.
        farm_id (int): The identifier of the farm where the duck is located.

    Config:
        json_schema_extra (dict): An example JSON object representing a duck.
    """

    id: int = None
    duck_name: str
    duck_type: str
    birthplace: str
    birthdate: date
    gender: str
    health_status: str
    farm_id: int

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Duck Model Configuration

        This class provides additional configuration options for the Duck model.

        Attributes:
            json_schema_extra (dict): A JSON object representing an example duck.
        """

        json_schema_extra = {
            "example": {
                "duck_name": "Bebek A",
                "duck_type": "Peking",
                "birthplace": "Kandang 1",
                "birthdate": "2022-05-15",
                "gender": "Betina",
                "health_status": "Sehat",
                "farm_id": 1,
            },
        }
