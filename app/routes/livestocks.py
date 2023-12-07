"""
This API provides functionalities to manage livestock records, including creating, retrieving,
updating, and deleting records.
"""
from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, status

import app.databases.location as db_lo
import app.databases.livestock as db_li
from app.schemas.livestock import Livestock
from app.auth.jwt import get_user

livestock_router = APIRouter(tags=["Livestocks"])


@livestock_router.post("/")
async def create_livestock(
    livestock: Livestock = Body(...), _: str = Depends(get_user)
) -> dict:
    """
    Creates a new livestock record in the database.

    Args:
        livestock: A Livestock object containing information about the new livestock.
        current_user: The currently authenticated user.

    Returns:
        A dictionary containing a success message and the ID of the newly created livestock record.
    
    Raises:
        HTTPException 404: If the specified location IDs (birthplace or current) do not exist.
        HTTPException 500: If an error occurs while creating the livestock record.
    """
    try:
        db_lo.get_location_by_id(livestock.location_id)
        db_lo.get_location_by_id(livestock.birthplace_id)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Location with supplied ID does not exist",
        ) from exc
    try:
        _id = db_li.create_livestock(livestock.to_db())
        return {"message": f"Livestock created successfully with ID {_id}"}
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create the livestock",
        ) from exc


@livestock_router.get("/", response_model=List[dict])
async def retrieve_all_livestocks(_: str = Depends(get_user)) -> List[dict]:
    """
    Retrieves a list of all livestock records from the database.

    Args:
        current_user: The currently authenticated user.

    Returns:
        A list of dictionaries, each representing a livestock record.
    """
    return db_li.get_livestocks()


@livestock_router.get("/{_id}", response_model=dict)
async def retrieve_livestock(_id: int, _: str = Depends(get_user)) -> dict:
    """
    Retrieves a specific livestock record by its ID.

    Args:
        _id: The ID of the livestock record to retrieve.
        current_user: The currently authenticated user.

    Returns:
        A dictionary representing the livestock record.

    Raises:
        HTTPException 404: If the livestock record with the given ID is not found.
    """
    livestock = db_li.get_livestock_by_id(_id)
    if livestock is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livestock with supplied ID does not exist",
        )
    return livestock


@livestock_router.patch("/{_id}", response_model=dict)
async def update_livestock(
    _id: int, updated_livestock: dict = Body(...), _: str = Depends(get_user)
) -> dict:
    """
    Updates an existing livestock record in the database.

    Args:
        _id: The ID of the livestock record to update.
        updated_livestock: A dictionary containing updated information for the livestock.
        current_user: The currently authenticated user.

    Returns:
        A dictionary containing a success message.

    Raises:
        HTTPException 404: If the livestock record with the given ID is not found.
    """
    try:
        db_li.update_livestock(_id, updated_livestock)
        return {"message": "Livestock updated successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livestock with supplied ID does not exist",
        ) from exc


@livestock_router.delete("/{_id}", response_model=dict)
async def delete_livestock(_id: int, _: str = Depends(get_user)) -> dict:
    """
    Deletes a livestock record from the database.

    Args:
        _id: The ID of the livestock record to delete.
        current_user: The currently authenticated user.

    Returns:
        A dictionary containing a success message.

    Raises:
        HTTPException 404: If the livestock record with the given ID is not found.
    """
    try:
        db_li.delete_livestock(_id)
        return {"message": "Livestock deleted successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livestock with supplied ID does not exist",
        ) from exc
