#!/usr/bin/python3
'''lists all State objects from the database'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    '''main function'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session
    sts = session.query(State).order_by(State.id).all()
    sessionmaker.close_all()


if __name__ == "__main__":
    main()
