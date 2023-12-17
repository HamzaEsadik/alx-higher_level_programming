#!/usr/bin/python3
"""script that changes the name of a State object from the database"""
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
    r = session.query(State).filter_by(id=2).first()
    r.name = "New Mexico"
    r = session.add(r)
    session.commit()
    session.close()
