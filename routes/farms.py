from fastapi import APIRouter, Body, HTTPException, status
from models.farms import Farm
from typing import List
import json

farm_router = APIRouter(tags=["Farms"])

with open("data.json", "r") as file:
    farms = json.load(file)["farms"]


@farm_router.get("/", response_model=List[Farm])
async def retrieve_all_farms() -> List[Farm]:
    return farms


@farm_router.get("/{id}", response_model=Farm)
async def retrieve_farm(id: int) -> Farm:
    for farm in farms:
        if farm.id == id:
            return farm
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Farm with supplied ID does not exist",
    )


@farm_router.post("/")
async def create_farm(body: Farm = Body(...)) -> dict:
    farms.append(farm)
    return {"message": "farm created successfully"}


@farm_router.delete("/{id}")
async def delete_farm(id: int) -> dict:
    for farm in farms:
        if farm.id == id:
            farms.remove(farm)
            return {"message": "farm deleted successfully"}
