"""
This module defines the FastAPI router for making predictions related to duck populations. It
includes functionality for predicting duck population trends for all ducks or for a specific farm
over the next three years.
"""

import json
import numpy as np
from fastapi import APIRouter, HTTPException, status
from sklearn.linear_model import LinearRegression

predict_router = APIRouter(tags=["Predicts"])


@predict_router.get("/", response_model=dict)
async def retrieve_all_predicts() -> dict:
    """
    Retrieve Predictions for All Ducks

    Retrieves predicted duck population trends for all ducks over the next three years.

    Returns:
        dict: A dictionary with the current duck population data and the predicted population for
        the next three years.
    """

    def predict_data(ducks_count):
        years = np.array(list(ducks_count.keys()))
        counts = np.array(list(ducks_count.values()))

        model = LinearRegression()
        model.fit(years.reshape(-1, 1), counts)
        max_year = np.max(years)
        predicted_years = np.arange(max_year + 1, max_year + 4).reshape(-1, 1)
        predicted_counts = model.predict(predicted_years)

        return dict(
            zip(
                predicted_years.flatten().tolist(),
                np.floor(predicted_counts).astype(int).tolist(),
            )
        )

    try:
        with open("app/ducks.json", "r", encoding="utf-8") as file:
            ducks = json.load(file)
        ducks_count = {}
        for duck in ducks:
            year = int(duck["birthdate"].split("-")[0])
            if year in ducks_count:
                ducks_count[year] += 1
            else:
                ducks_count[year] = 1
        if len(ducks_count) == 1:
            return {"message": "Not enough data to predict"}
        return {
            "message": "Predicted data for 3 years ahead",
            "current_data": ducks_count,
            "predicted_data": predict_data(ducks_count),
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farm with supplied ID does not exist",
        ) from e


@predict_router.get("/{farm_id}", response_model=dict)
async def retrieve_predict(farm_id: int) -> dict:
    """
    Retrieve Predictions for a Specific Farm

    Retrieves predicted duck population trends for a specific farm over the next three years.

    Args:
        farm_id (int): The unique ID of the farm for which predictions are requested.

    Returns:
        dict: A dictionary with the current duck population data for the specified farm and the
        predicted population for the next three years.
    """

    def predict_data(ducks_count):
        years = np.array(list(ducks_count.keys()))
        counts = np.array(list(ducks_count.values()))

        model = LinearRegression()
        model.fit(years.reshape(-1, 1), counts)
        max_year = np.max(years)
        predicted_years = np.arange(max_year + 1, max_year + 4).reshape(-1, 1)
        predicted_counts = model.predict(predicted_years)

        return dict(
            zip(
                predicted_years.flatten().tolist(),
                np.floor(predicted_counts).astype(int).tolist(),
            )
        )

    try:
        with open("app/ducks.json", "r", encoding="utf-8") as file:
            ducks = json.load(file)
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
        return {
            "message": "Predicted data for 3 years ahead",
            "current_data": ducks_count,
            "predicted_data": predict_data(ducks_count),
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farm with supplied ID does not exist",
        ) from e
