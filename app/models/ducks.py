from datetime import date
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DuckDB(Base):
    __tablename__ = "ducks"
    id = Column(Integer, primary_key=True)
    duck_name = Column(String(50), nullable=False)
    duck_type = Column(String(50), nullable=False)
    birthplace = Column(String(50), nullable=False)
    birthdate = Column(DateTime, nullable=False)
    gender = Column(String(6), nullable=False)
    health_status = Column(String(5), nullable=False)
    farm_id = Column(Integer, nullable=False)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "duck_name": self.duck_name,
            "duck_type": self.duck_type,
            "birthplace": self.birthplace,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "health_status": self.health_status,
            "farm_id": self.farm_id,
        }


class Duck(BaseModel):
    duck_name: str
    duck_type: str
    birthplace: str
    birthdate: date
    gender: str
    health_status: str
    farm_id: int

    def to_db(self) -> DuckDB:
        return DuckDB(**self.model_dump())

    # pylint: disable=too-few-public-methods
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
