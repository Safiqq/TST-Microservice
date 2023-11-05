from pydantic import BaseModel


class Farm(BaseModel):
    id: int
    farm_name: str
    farm_location: str
    number_of_barns: int
    total_capacity: int
    owner_name: str
    phone_number: str

    class Config:
        json_schema_extra = {
            "example": {
                "farm_name": "Peternakan XYZ",
                "farm_location": "Jl. Peternakan No. 456",
                "number_of_barns": 6,
                "total_capacity": 1500,
                "owner_name": "Jane Smith",
                "phone_number": "081234567891",
            },
        }
