#!/usr/bin/python3

"""7-model_state_fetch_all
Use the SQLAlchemy module to connect to a database and fetch records
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    dburl = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(dburl)
    result = engine.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = result.fetchall()

    for state in states:
        print(f"{state[0]}: {state[1]}")
