#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    # Retrieve all City objects and sort them by cities.id
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        state = session.query(State).filter(State.id == city.state_id).first()
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
