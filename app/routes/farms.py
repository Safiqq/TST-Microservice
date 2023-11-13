from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, status

import databases.farms as db
from models.farms import Farm
from auth.jwt import get_user

farm_router = APIRouter(tags=["Farms"])


@farm_router.post("/", response_model=dict)
async def create_farm(farm: Farm = Body(...), _: str = Depends(get_user)) -> dict:
    try:
        _id = db.create_farm(farm.to_db())
        return {"message": f"Farm created successfully with ID {_id}"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create the farm",
        ) from e


@farm_router.get("/", response_model=List[dict])
async def retrieve_all_farms(_: str = Depends(get_user)) -> List[dict]:
    return db.get_farms()


@farm_router.get("/{_id}", response_model=dict)
async def retrieve_farm(_id: int, _: str = Depends(get_user)) -> dict:
    try:
        return db.get_farm_by_id(_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farm with supplied ID does not exist",
        ) from e


@farm_router.put("/{_id}", response_model=dict)
async def update_farm(
    _id: int, updated_farm: Farm = Body(...), _: str = Depends(get_user)
) -> dict:
    try:
        db.update_farm(_id, updated_farm)
        return {"message": "Farm updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farm with supplied ID does not exist",
        ) from e


@farm_router.delete("/{_id}", response_model=dict)
async def delete_farm(_id: int, _: str = Depends(get_user)) -> dict:
    try:
        db.delete_farm(_id)
        return {"message": "Farm deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farm with supplied ID does not exist",
        ) from e
