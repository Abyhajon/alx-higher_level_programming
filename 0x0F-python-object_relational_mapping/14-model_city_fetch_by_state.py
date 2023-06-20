#!/usr/bin/python3

"""module - linking databases"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    State.cities = relationship("City",
                                order_by=City.id, back_populates="state")
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(argv[1],argv[2],argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City).filter(City.state_id ==
                                              State.id).all()
    for row in query:
        print("{}: {} {}".format(row[0].name, row[1].id, row[1].name))
    session.close()
