from fastapi import APIRouter, Body, HTTPException, status
from models.ducks import Duck
from typing import List
import json

duck_router = APIRouter(tags=["Ducks"])
with open("data.json", "r") as file:
    ducks = json.load(file)["ducks"]


@duck_router.get("/", response_model=List[Duck])
async def retrieve_all_ducks() -> List[Duck]:
    return ducks


@duck_router.get("/{id}", response_model=Duck)
async def retrieve_duck(id: int) -> Duck:
    for duck in ducks:
        if duck.id == id:
            return duck
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Duck with supplied ID does not exist",
    )


@duck_router.post("/")
async def create_duck(body: Duck = Body(...)) -> dict:
    ducks.append(duck)
    return {"message": "Duck created successfully"}


@duck_router.delete("/{id}")
async def delete_duck(id: int) -> dict:
    for duck in ducks:
        if duck.id == id:
            ducks.remove(duck)
            return {"message": "Duck deleted successfully"}
