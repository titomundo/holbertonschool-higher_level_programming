#!/usr/bin/python3

"""3-my_safe_filter_states
Uses the MySQLdb module to search in the database states based on user input
but safe from SQL Injections
"""

import MySQLdb
from sys import argv


def db_connection():
    """Connects to the database and allows to fetch data"""

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], password=argv[2], database=argv[3]
    )

    c = db.cursor()
    state = argv[4]
    query = """SELECT *
            FROM states
            WHERE states.name
            LIKE %s
            ORDER BY states.id ASC"""

    c.execute(query, (state,))
    result = c.fetchall()

    for i in result:
        print(i)

    c.close()
    db.close()


if __name__ == "__main__":
    db_connection()
