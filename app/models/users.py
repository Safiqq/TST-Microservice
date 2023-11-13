from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
        }


class User(BaseModel):
    username: str
    password: str

    def to_db(self):
        return UserDB(**self.model_dump())


class Token(BaseModel):
    access_token: str
    token_type: str

    def to_db(self):
        return UserDB(**self.model_dump())
