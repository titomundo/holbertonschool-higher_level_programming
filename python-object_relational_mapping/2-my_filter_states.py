#!/usr/bin/python3

"""2-my_filter_states
Uses the MySQLdb module to search in the database states based on user input
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
            LIKE '{}'
            ORDER BY states.id ASC""".format(state)

    c.execute(query)
    result = c.fetchall()

    for i in result:
        print(i)

    c.close()
    db.close()


if __name__ == "__main__":
    db_connection()
