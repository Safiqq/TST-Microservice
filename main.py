from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.ducks import duck_router
from routes.farms import farm_router
from routes.predict import predict_router

import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=[""],
)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


app.include_router(duck_router, prefix="/ducks")
app.include_router(farm_router, prefix="/farms")
app.include_router(predict_router, prefix="/predict")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
