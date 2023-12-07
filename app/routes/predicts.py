"""
This API provides functionalities to predict the number of livestock for the next three years based
on past data.
"""
import numpy as np
from fastapi import APIRouter, Depends, HTTPException, status
from sklearn.linear_model import LinearRegression

import app.databases.livestock as db
from app.auth.jwt import get_user

predict_router = APIRouter(tags=["Predicts"])


def predict_data(livestocks_count, _: str = Depends(get_user)):
    """
    Predicts the number of livestock for the next three years based on past data.

    Args:
        livestocks_count: A dictionary mapping years to counts of livestock for that year.
        _: A string representing the currently authenticated user. This is injected by the Depends
        decorator.

    Returns:
        A dictionary mapping predicted years to predicted counts of livestock.
    """
    years = np.array(list(livestocks_count.keys()))
    counts = np.array(list(livestocks_count.values()))

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


@predict_router.get("/", response_model=dict)
async def retrieve_all_predicts(_: str = Depends(get_user)) -> dict:
    """
    Retrieves predicted data for all livestock across all locations.

    Args:
        _: A string representing the currently authenticated user. This is injected by the Depends
        decorator.

    Returns:
        A dictionary containing a message, a dictionary of current year data, and a dictionary of
        predicted year data.
    
    Raises:
        HTTPException 404: If there is not enough data to make a prediction.
    """
    livestocks = db.get_livestocks()
    livestocks_count = {}
    for livestock in livestocks:
        year = int(livestock.get("birthdate").isoformat().split("-")[0])
        if year in livestocks_count:
            livestocks_count[year] += 1
        else:
            livestocks_count[year] = 1
    if len(livestocks_count) <= 1:
        return {"message": "Not enough data to predict"}
    return {
        "message": "Predicted data for 3 years ahead",
        "current_data": livestocks_count,
        "predicted_data": predict_data(livestocks_count),
    }


@predict_router.get("/{location_id}", response_model=dict)
async def retrieve_predict(location_id: int, _: str = Depends(get_user)) -> dict:
    """
    Retrieves predicted data for livestock at a specific location.

    Args:
        location_id: The ID of the location for which to predict the number of livestock.
        _: A string representing the currently authenticated user. This is injected by the Depends
        decorator.

    Returns:
        A dictionary containing a message, a dictionary of current year data, and a dictionary of
        predicted year data.
    
    Raises:
        HTTPException 404: If the location with the supplied ID does not exist.
    """
    try:
        livestocks = db.get_livestocks()
        livestocks_count = {}
        for livestock in livestocks:
            if livestock.get("location_id") == location_id:
                year = int(livestock.get("birthdate").isoformat().split("-")[0])
                if year in livestocks_count:
                    livestocks_count[year] += 1
                else:
                    livestocks_count[year] = 1
        if len(livestocks_count) <= 1:
            return {"message": "Not enough data to predict"}
        return {
            "message": "Predicted data for 3 years ahead",
            "current_data": livestocks_count,
            "predicted_data": predict_data(livestocks_count),
        }
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Location with supplied ID does not exist",
        ) from exc
