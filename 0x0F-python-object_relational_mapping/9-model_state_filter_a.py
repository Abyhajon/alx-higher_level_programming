#!/usr/bin/python3
"""
Script that lists all State objects
containing the letter 'a' from the database hbtn_0e_6_usa

"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Get MySQL username, password,
    # and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create connection URL
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name)

    # Create engine and bind it to the Base class
    engine = create_engine(url)
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all State objects containing the
    # letter 'a' and sort them by states.id
    states = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
