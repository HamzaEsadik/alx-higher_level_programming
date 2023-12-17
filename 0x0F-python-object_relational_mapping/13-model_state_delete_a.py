#!/usr/bin/python3
"""
script that deletes all State objects with a name
containing the letter a from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(
                                        sys.argv[1],
                                        sys.argv[2],
                                        sys.argv[3]
                                            ),
                            pool_pre_ping=True
                                )
    session = Session(engine)
    r = session.query(State).filter(State.name.like('%a%'))
    for row in r:
        session.delete(row)
    session.commit()
    session.close()
