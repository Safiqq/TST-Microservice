"""
This is a FastAPI application that provides endpoints for managing ducks, farms, and making
predictions.

It includes CORS middleware to allow cross-origin requests and defines several routes for different
functionalities.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.ducks import duck_router
from routes.farms import farm_router
from routes.predicts import predict_router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=[""],
)


@app.get("/", response_model=dict)
async def root() -> dict:
    """
    Root Endpoint

    Returns a simple message when you access the root URL.

    Returns:
        dict: A dictionary with a message.
    """
    return {"message": "Hello, World!"}


app.include_router(duck_router, prefix="/ducks")
app.include_router(farm_router, prefix="/farms")
app.include_router(predict_router, prefix="/predicts")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
