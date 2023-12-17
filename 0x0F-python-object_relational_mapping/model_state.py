#!/usr/bin/python3
'''model state mudule'''
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    '''
    State class.

    attribites:
        -id: the id
        -name: state name
    '''
    __tablename__ = "states"

    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
