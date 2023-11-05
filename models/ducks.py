from pydantic import BaseModel
from datetime import date


class Duck(BaseModel):
    id: int
    duck_name: str
    duck_type: str
    birthplace: str
    birthdate: date
    gender: str
    health_status: str
    farm_id: int

    class Config:
        json_schema_extra = {
            "example": {
                "duck_name": "Bebek A",
                "duck_type": "Peking",
                "birthplace": "Kandang 1",
                "birthdate": "2022-05-15",
                "gender": "Betina",
                "health_status": "Sehat",
                "farm_id": 1,
            },
        }
