#!/usr/bin/python3

"""7-model_state_fetch_all
Use the SQLAlchemy module to connect to a database and fetch records
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    dburl = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(dburl)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print(f"{instance.id}: {instance.name}")

    session.close()
