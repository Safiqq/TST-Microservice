"""
This module defines the SQLAlchemy model used to manage user data within the application.
"""
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# pylint: disable-next=too-few-public-methods
class UserDB(Base):
    """
    Represents a user record in the database.

    Attributes:
        id: The unique identifier of the user.
        username: The username of the user.
        password: The hashed password of the user.
        admin: True if the user has admin privileges, False otherwise.
    """

    __tablename__ = "user"
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(25), unique=True, nullable=False)
    password = sa.Column(sa.String(255), nullable=False)
    admin = sa.Column(sa.Boolean, default=False)

    def to_dict(self) -> dict:
        """
        Converts the user record to a dictionary representation.

        Returns:
            A dictionary containing information about the user, excluding the password.
        """
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "admin": self.admin,
        }
