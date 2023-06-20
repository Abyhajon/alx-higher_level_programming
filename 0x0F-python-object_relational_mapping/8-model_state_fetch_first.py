#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
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

    # Retrieve the first State object based on states.id
    first_state = session.query(State).order_by(State.id).first()

    # Check if the table is empty
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    # Close the session
    session.close()
