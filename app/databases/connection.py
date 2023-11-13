from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import *

engine = create_engine(config.get("DB_URL"))

Base = declarative_base()
Base.metadata.create_all(engine)

Session = sessionmaker(engine)

Base = declarative_base()

sess = Session()