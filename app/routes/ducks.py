from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, status

import databases.ducks as db
import databases.farms as db
from models.ducks import Duck
from auth.jwt import get_user

duck_router = APIRouter(tags=["Ducks"])


@duck_router.post("/")
async def create_duck(duck: Duck = Body(...), _: str = Depends(get_user)) -> dict:
    farm = db.get_farm_by_id(duck.farm_id)
    if farm is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Farm with supplied ID does not exist",
        )
    try:
        _id = db.create_duck(duck.to_db())
        return {"message": f"Duck created successfully with ID {_id}"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create the duck",
        ) from e


@duck_router.get("/", response_model=List[dict])
async def retrieve_all_ducks(_: str = Depends(get_user)) -> List[dict]:
    return db.get_ducks()


@duck_router.get("/{_id}", response_model=dict)
async def retrieve_duck(_id: int, _: str = Depends(get_user)) -> dict:
    try:
        return db.get_duck_by_id(_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Duck with supplied ID does not exist",
        ) from e


@duck_router.put("/{_id}", response_model=dict)
async def update_duck(
    _id: int, updated_duck: Duck = Body(...), _: str = Depends(get_user)
) -> dict:
    try:
        db.update_duck(_id, updated_duck)
        return {"message": "Duck updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Duck with supplied ID does not exist",
        ) from e


@duck_router.delete("/{_id}", response_model=dict)
async def delete_duck(_id: int, _: str = Depends(get_user)) -> dict:
    try:
        db.delete_duck(_id)
        return {"message": "Duck deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Duck with supplied ID does not exist",
        ) from e
