"""
This module defines the SQLAlchemy models used to manage location and livestock data within the
application.
"""
import uuid
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship, mapped_column

Base = declarative_base()


# pylint: disable-next=too-few-public-methods
class LocationDB(Base):
    """
    Represents a location record in the database.

    Attributes:
        id: The unique identifier of the location.
        type: The type of the location (farm, market, warehouse).
        name: The name of the location.
        address: The address of the location.
    """

    __tablename__ = "location"
    id = mapped_column(sa.Integer, primary_key=True)
    type = mapped_column(sa.Enum("farm", "market", "warehouse"), nullable=False)
    name = mapped_column(sa.String(100), nullable=False)
    address = mapped_column(sa.String(255), nullable=False)

    # pylint: disable-next=too-few-public-methods
    def to_dict(self) -> dict:
        """
        Converts the location record to a dictionary representation.

        Returns:
            A dictionary containing information about the location.
        """
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "address": self.address,
        }


# pylint: disable-next=too-few-public-methods
class LivestockDB(Base):
    """
    Represents a livestock record in the database.

    Attributes:
        id: The unique identifier of the livestock.
        name: The name of the livestock.
        breed: The breed of the livestock.
        species: The species of the livestock.
        birthplace_id: The foreign key referencing the birthplace location.
        birthdate: The date of birth of the livestock.
        gender: The gender of the livestock (male, female).
        location_id: The foreign key referencing the current location.

    Relationships:
        birthplace: The LocationDB object representing the birthplace.
        location: The LocationDB object representing the current location.
    """

    __tablename__ = "livestock"
    # id = mapped_column(sa.Integer, primary_key=True)
    id = mapped_column(sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = mapped_column(sa.String(50), nullable=False)
    breed = mapped_column(sa.String(50), nullable=False)
    species = mapped_column(sa.String(50), nullable=False)
    birthplace_id = mapped_column(
        sa.Integer, sa.ForeignKey("location.id"), nullable=False
    )
    birthdate = mapped_column(sa.DateTime, nullable=False)
    gender = mapped_column(sa.Enum("male", "female"), nullable=False)
    location_id = mapped_column(
        sa.Integer, sa.ForeignKey("location.id"), nullable=False
    )

    birthplace = relationship("LocationDB", foreign_keys=[birthplace_id])
    location = relationship("LocationDB", foreign_keys=[location_id])

    def to_dict(self) -> dict:
        """
        Converts the livestock record to a dictionary representation.

        Returns:
            A dictionary containing information about the livestock.
        """
        return {
            "id": self.id,
            "name": self.name,
            "breed": self.breed,
            "species": self.species,
            "birthplace_id": self.birthplace_id,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "location_id": self.location_id,
        }
