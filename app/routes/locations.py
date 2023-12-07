"""
This API provides functionalities to manage location records, including creating, retrieving,
updating, and deleting records.
"""
from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, status

import app.databases.location as db
from app.schemas.location import Location
from app.auth.jwt import get_user

location_router = APIRouter(tags=["Locations"])


@location_router.post("/", response_model=dict)
async def create_location(
    location: Location = Body(...), _: str = Depends(get_user)
) -> dict:
    """
    Creates a new location record in the database.

    Args:
        location: A Location object containing information about the new location.
        current_user: The currently authenticated user.

    Returns:
        A dictionary containing a success message and the ID of the newly created location record.
    
    Raises:
        HTTPException 500: If an error occurs while creating the location record.
    """
    try:
        _id = db.create_location(location.to_db())
        return {"message": f"Location created successfully with ID {_id}"}
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create the location",
        ) from exc


@location_router.get("/", response_model=List[dict])
async def retrieve_all_locations(_: str = Depends(get_user)) -> List[dict]:
    """
    Retrieves a list of all location records from the database.

    Args:
        current_user: The currently authenticated user.

    Returns:
        A list of dictionaries, each representing a location record.
    """
    return db.get_locations()


@location_router.get("/{_id}", response_model=dict)
async def retrieve_location(_id: int, _: str = Depends(get_user)) -> dict:
    """
    Retrieves a specific location record by its ID.

    Args:
        _id: The ID of the location record to retrieve.
        current_user: The currently authenticated user.

    Returns:
        A dictionary representing the location record.

    Raises:
        HTTPException 404: If the location record with the given ID is not found.
    """
    location = db.get_location_by_id(_id)
    if location is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Location with supplied ID does not exist",
        )
    return location


@location_router.patch("/{_id}", response_model=dict)
async def update_location(
    _id: int, updated_location: dict = Body(...), _: str = Depends(get_user)
) -> dict:
    """
    Updates an existing location record in the database.

    Args:
        _id: The ID of the location record to update.
        updated_location: A dictionary containing updated information for the location.
        current_user: The currently authenticated user.

    Returns:
        A dictionary containing a success message.

    Raises:
        HTTPException 404: If the location record with the given ID is not found.
    """
    try:
        db.update_location(_id, updated_location)
        return {"message": "Location updated successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Location with supplied ID does not exist",
        ) from exc


@location_router.delete("/{_id}", response_model=dict)
async def delete_location(_id: int, _: str = Depends(get_user)) -> dict:
    """
    Deletes a location record from the database.

    Args:
        _id: The ID of the location record to delete.
        current_user: The currently authenticated user.

    Returns:
        A dictionary containing a success message.

    Raises:
        HTTPException 404: If the location record with the given ID is not found.
    """
    try:
        db.delete_location(_id)
        return {"message": "Location deleted successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Location with supplied ID does not exist",
        ) from exc
