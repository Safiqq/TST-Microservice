"""
Main module for the FastAPI application.

This module defines the application instance, configures middleware, defines exception handlers,
and includes routers for different functionalities:

- User management
- Location management
- Livestock management
- Prediction generation

"""
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.routes.users import user_router
from app.routes.locations import location_router
from app.routes.livestocks import livestock_router
from app.routes.predicts import predict_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=[""],
)


@app.exception_handler(RequestValidationError)
# pylint: disable-next=unused-argument
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Handles validation errors raised by FastAPI.

    Args:
        request: The request object.
        exc: The exception object.

    Returns:
        JSONResponse: A JSON response containing the error details.
    """
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.get("/", response_model=dict)
async def root() -> dict:
    """
    Returns a root message.

    Returns:
        dict: A dictionary containing the message.
    """
    return {
        "message": [
            '       ,6*"*VA.                                              ,6*"*VA. ',
            " __,  dN     V8                   __,                       dN     V8 ",
            '`7MM  `MN.  ,g9 pd*"*b.  pd*"*b. `7MM  ,pP\' "Yq.       ,AM   `MN.  ,g9 ',
            "  MM   ,MMMMq. (O)   j8 (O)   j8   MM 6W'    `Wb     AVMM    ,MMMMq.  ",
            "  MM  6P   `YMb    ,;j9     ,;j9   MM 8M      M8   ,W' MM   6P   `YMb ",
            "  MM  8b    `M9 ,-='     ,-='      MM YA.    ,A9 ,W'   MM   8b    `M9 ",
            ".JMML.`MmmmmM9 Ammmmmmm Ammmmmmm .JMML.`Ybmmd9'  AmmmmmMMmm `MmmmmM9  ",
            "                                                       MM             ",
            "                                                       MM             ",
        ]
    }


app.include_router(user_router)
app.include_router(location_router, prefix="/locations")
app.include_router(livestock_router, prefix="/livestocks")
app.include_router(predict_router, prefix="/predicts")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
