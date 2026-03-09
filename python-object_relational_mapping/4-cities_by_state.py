#!/usr/bin/python3

"""4-cities_by_state
Uses the MySQLdb module to search in the database cities table
"""

import MySQLdb
from sys import argv


def db_connection():
    """Connects to the database and allows to fetch data"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3],
    )

    c = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states
            ON state_id = states.id
            ORDER BY cities.id ASC"""

    c.execute(query)
    result = c.fetchall()

    for i in result:
        print(i)

    c.close()
    db.close()


if __name__ == "__main__":
    db_connection()
