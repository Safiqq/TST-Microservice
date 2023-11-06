"""
This module defines the FastAPI router for managing duck-related endpoints. It includes
functionality for creating, retrieving, updating, and deleting ducks.
"""

import json
from typing import List
from fastapi import APIRouter, Body, HTTPException, status

from models.ducks import Duck

duck_router = APIRouter(tags=["Ducks"])
with open("app/ducks.json", "r", encoding="utf-8") as file:
    ducks = json.load(file)


@duck_router.post("/")
async def create_duck(duck: Duck = Body(...)) -> dict:
    """
    Create a Duck

    Creates a new duck in the system and updates the JSON data file.

    Args:
        duck (Duck): The Duck object to create.

    Returns:
        dict: A message indicating the successful creation of the duck.
    """
    try:
        max_id = max(_duck["id"] for _duck in ducks) if ducks else 0
        duck = dict(
            Duck(
                id=max_id + 1,
                duck_name=duck.duck_name,
                duck_type=duck.duck_type,
                birthplace=duck.birthplace,
                birthdate=duck.birthdate,
                gender=duck.gender,
                health_status=duck.health_status,
                farm_id=duck.farm_id,
            )
        )
        duck["birthdate"] = duck["birthdate"].isoformat()
        ducks.append(duck)
        with open("app/ducks.json", "w", encoding="utf-8") as _file:
            json.dump(ducks, _file, ensure_ascii=False, indent=4)
        return {"message": f"Duck created successfully with ID {max_id + 1}"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create the duck.",
        ) from e


@duck_router.get("/", response_model=List[Duck])
async def retrieve_all_ducks() -> List[Duck]:
    """
    Retrieve All Ducks

    Returns a list of all ducks available in the system.

    Returns:
        List[Duck]: A list of Duck objects.
    """
    return ducks


@duck_router.get("/{_id}", response_model=Duck)
async def retrieve_duck(_id: int) -> Duck:
    """
    Retrieve a Duck by ID

    Retrieves a duck by its unique identifier (ID).

    Args:
        _id (int): The unique ID of the duck to retrieve.

    Returns:
        Duck: The Duck object with the specified ID.

    Raises:
        HTTPException: If a duck with the supplied ID does not exist, it returns a 404 Not Found
        response.
    """
    for duck in ducks:
        if duck["id"] == _id:
            return duck
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Duck with supplied ID does not exist",
    )


@duck_router.put("/{_id}", response_model=dict)
async def update_duck(_id: int, updated_duck: Duck = Body(...)) -> dict:
    """
    Update a Duck by ID

    Updates an existing duck in the system based on its unique identifier (ID).

    Args:
        _id (int): The unique ID of the duck to update.
        updated_duck (Duck): The updated Duck object.

    Returns:
        dict: A message indicating the successful update of the duck.
    """
    for duck in ducks:
        if duck["id"] == _id:
            ducks.remove(duck)
            updated_duck = dict(
                Duck(
                    id=_id,
                    duck_name=updated_duck.duck_name,
                    duck_type=updated_duck.duck_type,
                    birthplace=updated_duck.birthplace,
                    birthdate=updated_duck.birthdate,
                    gender=updated_duck.gender,
                    health_status=updated_duck.health_status,
                    farm_id=updated_duck.farm_id,
                )
            )
            updated_duck["birthdate"] = updated_duck["birthdate"].isoformat()
            ducks.append(updated_duck)
            with open("app/ducks.json", "w", encoding="utf-8") as _file:
                json.dump(ducks, _file, ensure_ascii=False, indent=4)
            return {"message": "Duck updated successfully"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Duck with supplied ID does not exist",
    )


@duck_router.delete("/{_id}", response_model=dict)
async def delete_duck(_id: int) -> dict:
    """
    Delete a Duck by ID

    Deletes a duck from the system based on its unique identifier (ID).

    Args:
        _id (int): The unique ID of the duck to delete.

    Returns:
        dict: A message indicating the successful deletion of the duck.
    """
    for duck in ducks:
        if duck["id"] == _id:
            ducks.remove(duck)
            with open("app/ducks.json", "w", encoding="utf-8") as _file:
                json.dump(ducks, _file, ensure_ascii=False, indent=4)
            return {"message": "Duck deleted successfully"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Duck with supplied ID does not exist",
    )
