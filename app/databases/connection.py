"""
This module initializes the SQLAlchemy database connection and session manager for the application.

- `engine`: Creates a SQLAlchemy engine instance using the database connection URL from the
            configuration.
- `Base`: Defines a declarative base class for SQLAlchemy models to inherit from.
- `metadata`: Creates all the database tables based on the models.
- `Session`: Creates a sessionmaker object to create database sessions.
- `sess`: Creates a global database session object for use throughout the application.

"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import config

engine = create_engine(config.get("DB_URL"))

Base = declarative_base()
Base.metadata.create_all(engine)

Session = sessionmaker(engine)

sess = Session()
