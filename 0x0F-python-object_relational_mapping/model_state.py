#!/usr/bin/python3
'''model state mudule'''
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

connection_string = 'mysql://root:usopp@localhost:3306/hbtn_0e_6_usa'
engine = create_engine(connection_string, echo=True)
engine.connect()

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
