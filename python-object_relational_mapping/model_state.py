#!/usr/bin/python3

"""model_state:
Class model for State. This class will be used to generate ORM models
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    Inherits from base class. Used to connect to the states table
    in the database
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
