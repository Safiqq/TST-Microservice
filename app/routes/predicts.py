import numpy as np
from fastapi import APIRouter, Depends, HTTPException, status
from sklearn.linear_model import LinearRegression

import databases.ducks as db
from auth.jwt import get_user

predict_router = APIRouter(tags=["Predicts"])


def predict_data(ducks_count, _: str = Depends(get_user)):
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


@predict_router.get("/", response_model=dict)
async def retrieve_all_predicts(_: str = Depends(get_user)) -> dict:
    ducks = db.get_ducks()
    ducks_count = {}
    for duck in ducks:
        year = int(duck.get("birthdate").isoformat().split("-")[0])
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


@predict_router.get("/{farm_id}", response_model=dict)
async def retrieve_predict(farm_id: int, _: str = Depends(get_user)) -> dict:
    try:
        ducks = db.get_ducks()
        ducks_count = {}
        for duck in ducks:
            if duck.get("farm_id") == farm_id:
                year = int(duck.get("birthdate").isoformat().split("-")[0])
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
