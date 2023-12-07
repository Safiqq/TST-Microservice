"""
This module provides functions for managing livestock data within the application.
"""
from typing import List
from app.models.model import LivestockDB
from app.schemas.livestock import Livestock
from app.databases.connection import sess


def create_livestock(new_livestock: Livestock) -> int:
    """
    Creates a new livestock record in the database.

    Args:
        new_livestock: A Livestock object containing information about the new livestock.

    Returns:
        The ID of the newly created livestock record.
    """
    sess.add(new_livestock)
    sess.commit()
    new_livestock_id = new_livestock.id
    sess.close()
    return new_livestock_id


def get_livestocks() -> List[dict]:
    """
    Retrieves a list of all livestock records from the database.

    Returns:
        A list of dictionaries, each representing a livestock record.
    """
    livestocks = sess.query(LivestockDB).order_by(LivestockDB.id).all()
    livestocks_dict = []
    for i in livestocks:
        livestocks_dict.append(i.to_dict())
    return livestocks_dict


def get_livestock_by_id(_id: int) -> dict:
    """
    Retrieves a specific livestock record by its ID.

    Args:
        _id: The ID of the livestock record to retrieve.

    Returns:
        A dictionary representing the livestock record, or None if no record is found.
    """
    livestock = sess.query(LivestockDB).filter(LivestockDB.id == _id).first()
    if livestock:
        return livestock.to_dict()
    return None


def update_livestock(_id: int, updated_livestock: dict) -> dict:
    """
    Updates an existing livestock record in the database.

    Args:
        _id: The ID of the livestock record to update.
        updated_livestock: A dictionary containing updated information for the livestock.

    Returns:
        A dictionary representing the updated livestock record.
    """
    livestock = sess.query(LivestockDB).filter(LivestockDB.id == _id).first()

    if "name" in updated_livestock:
        livestock.name = updated_livestock["name"]
    if "breed" in updated_livestock:
        livestock.breed = updated_livestock["breed"]
    if "species" in updated_livestock:
        livestock.species = updated_livestock["species"]
    if "birthplace_id" in updated_livestock:
        livestock.birthplace_id = updated_livestock["birthplace_id"]
    if "birthdate" in updated_livestock:
        livestock.birthdate = updated_livestock["birthdate"]
    if "gender" in updated_livestock:
        livestock.gender = updated_livestock["gender"]
    if "location_id" in updated_livestock:
        livestock.location_id = updated_livestock["location_id"]

    sess.commit()
    livestock_dict = livestock.to_dict()
    sess.close()
    return livestock_dict


def delete_livestock(_id: int) -> int:
    """
    Deletes a livestock record from the database.

    Args:
        _id: The ID of the livestock record to delete.

    Returns:
        The ID of the deleted livestock record.
    """
    livestock = sess.query(LivestockDB).filter(LivestockDB.id == _id).first()
    sess.delete(livestock)
    sess.commit()
    sess.close()
    return _id
