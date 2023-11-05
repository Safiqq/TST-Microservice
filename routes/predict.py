from fastapi import APIRouter, Body, HTTPException, status
from typing import List
import json
import numpy as np
from sklearn.linear_model import LinearRegression

predict_router = APIRouter(tags=["Ducks"])

with open("data.json", "r") as file:
    data = json.load(file)
    ducks = data["ducks"]
    farms = data["farms"]


@predict_router.get("/{farm_id}")
async def retrieve_duck(farm_id: int):
    def predict_data(ducks_count):
        years = np.array(list(ducks_count.keys()))
        counts = np.array(list(ducks_count.values()))

        model = LinearRegression()
        model.fit(years.reshape(-1, 1), counts)
        max_year = np.max(years)
        predicted_years = np.arange(max_year + 1, max_year + 4).reshape(-1, 1)
        predicted_counts = model.predict(predicted_years)

        for year, count in zip(predicted_years.flatten(), predicted_counts):
            print(f"Year {year}: Predicted Population = {count:.2f}")

    ducks_count = {}
    for duck in ducks:
        if duck["farm_id"] == farm_id:
            year = int(duck["birthdate"].split("-")[0])
            if year in ducks_count:
                ducks_count[year] += 1
            else:
                ducks_count[year] = 1
    if len(ducks_count) == 1:
        return {"message": "Not enough data to predict"}
    else:
        predict_data(ducks_count)
        return {
            f"message": "Predicted data for 3 years ahead",
            "predicted_data": ducks_count,
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Farm with supplied ID does not exist",
    )
