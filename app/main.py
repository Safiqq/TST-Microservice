from fastapi.security import OAuth2PasswordBearer
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.users import user_router
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
    return {
        "message": [
            '       ,6*"*VA.                                              ,6*"*VA. ',
            " __,  dN     V8                   __,                       dN     V8 ",
            '`7MM  `MN.  ,g9 pd*"*b.  pd*"*b. `7MM  ,pP' "Yq.       ,AM   `MN.  ,g9 ",
            "  MM   ,MMMMq. (O)   j8 (O)   j8   MM 6W'    `Wb     AVMM    ,MMMMq.  ",
            "  MM  6P   `YMb    ,;j9     ,;j9   MM 8M      M8   ,W' MM   6P   `YMb ",
            "  MM  8b    `M9 ,-='     ,-='      MM YA.    ,A9 ,W'   MM   8b    `M9 ",
            ".JMML.`MmmmmM9 Ammmmmmm Ammmmmmm .JMML.`Ybmmd9'  AmmmmmMMmm `MmmmmM9  ",
            "                                                       MM             ",
            "                                                       MM             ",
        ]
    }


app.include_router(user_router)
app.include_router(duck_router, prefix="/ducks")
app.include_router(farm_router, prefix="/farms")
app.include_router(predict_router, prefix="/predicts")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
