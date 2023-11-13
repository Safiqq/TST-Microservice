from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class FarmDB(Base):
    __tablename__ = "farms"
    id = Column(Integer, primary_key=True)
    farm_name = Column(String(50), nullable=False)
    farm_location = Column(String(50), nullable=False)
    number_of_barns = Column(Integer, nullable=False)
    total_capacity = Column(Integer, nullable=False)
    owner_name = Column(String(50), nullable=False)
    phone_number = Column(String(16), nullable=False)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "farm_name": self.farm_name,
            "farm_location": self.farm_location,
            "number_of_barns": self.number_of_barns,
            "total_capacity": self.total_capacity,
            "owner_name": self.owner_name,
            "phone_number": self.phone_number,
        }


class Farm(BaseModel):
    farm_name: str
    farm_location: str
    number_of_barns: int
    total_capacity: int
    owner_name: str
    phone_number: str

    def to_db(self) -> FarmDB:
        return FarmDB(**self.model_dump())

    # pylint: disable=too-few-public-methods
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
