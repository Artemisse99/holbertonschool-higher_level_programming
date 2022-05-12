#!/usr/bin/python3
"""
First state model
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """First state model"""

    __tablename__ = 'states'

    id = Column(Integer,
                autoincrement=True,
                primary_key=True,
                nullable=False)

    name = Column(String(128),
                  nullable=False)
