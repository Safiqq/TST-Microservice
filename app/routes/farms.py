"""
This module defines the FastAPI router for managing farm-related endpoints. It includes
functionality for retrieving all farms, retrieving a single farm by ID, creating a new farm, and
deleting a farm.
"""

import json
from typing import List
from fastapi import APIRouter, Body, HTTPException, status

from models.farms import Farm

farm_router = APIRouter(tags=["Farms"])
with open("app/farms.json", "r", encoding="utf-8") as file:
    farms = json.load(file)


@farm_router.post("/", response_model=dict)
async def create_farm(farm: Farm = Body(...)) -> dict:
    """
    Create a Farm

    Creates a new farm in the system and updates the JSON data file.

    Args:
        farm (Farm): The Farm object to create.

    Returns:
        dict: A message indicating the successful creation of the farm.
    """
    try:
        max_id = max(_farm["id"] for _farm in farms) if farms else 0
        farm = dict(
            Farm(
                id=max_id + 1,
                farm_name=farm.farm_name,
                farm_location=farm.farm_location,
                number_of_barns=farm.number_of_barns,
                total_capacity=farm.total_capacity,
                owner_name=farm.owner_name,
                phone_number=farm.phone_number,
            )
        )
        farms.append(farm)
        with open("app/farms.json", "w", encoding="utf-8") as _file:
            json.dump(farms, _file, ensure_ascii=False, indent=4)
        return {"message": f"Farm created successfully with ID {max_id + 1}"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create the farm.",
        ) from e


@farm_router.get("/", response_model=List[Farm])
async def retrieve_all_farms() -> List[Farm]:
    """
    Retrieve All Farms

    Returns a list of all farms available in the system.

    Returns:
        List[Farm]: A list of Farm objects.
    """
    return farms


@farm_router.get("/{_id}", response_model=Farm)
async def retrieve_farm(_id: int) -> Farm:
    """
    Retrieve a Farm by ID

    Retrieves a farm by its unique identifier (ID).

    Args:
        _id (int): The unique ID of the farm to retrieve.

    Returns:
        Farm: The Farm object with the specified ID.

    Raises:
        HTTPException: If a farm with the supplied ID does not exist, it returns a 404 Not Found
        response.
    """
    for farm in farms:
        if farm["id"] == _id:
            return farm
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Farm with supplied ID does not exist",
    )


@farm_router.put("/{_id}", response_model=dict)
async def update_farm(_id: int, updated_farm: Farm = Body(...)) -> dict:
    """
    Update a Farm by ID

    Updates an existing farm in the system based on its unique identifier (ID).

    Args:
        _id (int): The unique ID of the farm to update.
        updated_farm (Farm): The updated Farm object.

    Returns:
        dict: A message indicating the successful update of the farm.
    """
    for farm in farms:
        if farm["id"] == _id:
            farms.remove(farm)
            updated_farm = dict(
                Farm(
                    id=_id,
                    farm_name=updated_farm.farm_name,
                    farm_location=updated_farm.farm_location,
                    number_of_barns=updated_farm.number_of_barns,
                    total_capacity=updated_farm.total_capacity,
                    owner_name=updated_farm.owner_name,
                    phone_number=updated_farm.phone_number,
                )
            )
            farms.append(updated_farm)
            with open("app/farms.json", "w", encoding="utf-8") as _file:
                json.dump(farms, _file, ensure_ascii=False, indent=4)
            return {"message": "Farm updated successfully"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Farm with supplied ID does not exist",
    )


@farm_router.delete("/{_id}", response_model=dict)
async def delete_farm(_id: int) -> dict:
    """
    Delete a Farm by ID

    Deletes a farm from the system based on its unique identifier (ID).

    Args:
        _id (int): The unique ID of the farm to delete.

    Returns:
        dict: A message indicating the successful deletion of the farm.
    """
    for farm in farms:
        if farm["id"] == _id:
            farms.remove(farm)
            with open("app/farms.json", "w", encoding="utf-8") as _file:
                json.dump(farms, _file, ensure_ascii=False, indent=4)
            return {"message": "Farm deleted successfully"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Farm with supplied ID does not exist",
    )
