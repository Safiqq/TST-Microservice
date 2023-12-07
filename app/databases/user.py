"""
This module provides functions for managing user data within the application.
"""
from typing import List
from app.models.user import UserDB
from app.databases.connection import sess
from app.schemas.user import User


def create_user(new_user: UserDB) -> int:
    """
    Creates a new user record in the database.

    Args:
        new_user: A UserDB object containing information about the new user.

    Returns:
        The ID of the newly created user record.
    """
    sess.add(new_user)
    sess.commit()
    new_user_id = new_user.id
    sess.close()
    return new_user_id


def get_users() -> List[dict]:
    """
    Retrieves a list of all user records from the database.

    Returns:
        A list of dictionaries, each representing a user record.
    """
    users = sess.query(UserDB).order_by(UserDB.id).all()
    users_dict = []
    for i in users:
        users_dict.append(i.to_dict())
    return users_dict


def get_user_by_username(username: str) -> dict:
    """
    Retrieves a specific user record by its username.

    Args:
        username: The username of the user to retrieve.

    Returns:
        A dictionary representing the user record, or None if no record is found.
    """
    user = sess.query(UserDB).filter(UserDB.username == username).first()
    if user:
        return user.to_dict()
    return user


def update_user(_id: int, updated_user: User) -> dict:
    """
    Updates an existing user record in the database.

    Args:
        _id: The ID of the user record to update.
        updated_user: A User object containing updated information for the user.

    Returns:
        A dictionary representing the updated user record.
    """
    user = sess.query(UserDB).filter(UserDB.id == _id).first()

    user.user_name = updated_user.user_name
    user.user_location = updated_user.user_location
    user.number_of_barns = updated_user.number_of_barns
    user.total_capacity = updated_user.total_capacity
    user.owner_name = updated_user.owner_name
    user.phone_number = updated_user.phone_number

    sess.commit()
    user_dict = user.to_dict()
    sess.close()
    return user_dict


def delete_user(_id: int) -> int:
    """
    Deletes a user record from the database.

    Args:
        _id: The ID of the user record to delete.

    Returns:
        The ID of the deleted user record.
    """
    user = sess.query(UserDB).filter(UserDB.id == _id).first()
    sess.delete(user)
    sess.commit()
    sess.close()
    return _id
