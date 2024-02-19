#!/usr/bin/python3
'''class definition of a State'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
