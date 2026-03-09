#!/usr/bin/python3

"""5-filter_cities
Uses the MySQLdb module to search in the database and returns the cities
related to a user-specified state
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

    state = argv[4]
    c = db.cursor()
    query = """SELECT cities.name
            FROM cities
            INNER JOIN states ON state_id = states.id
            WHERE states.name LIKE %s
            ORDER BY cities.id ASC"""

    c.execute(query, (state,))
    result = c.fetchall()
    cities = [i[0] for i in result]
    print(*cities, sep=", ", end="\n")

    c.close()
    db.close()


if __name__ == "__main__":
    db_connection()
