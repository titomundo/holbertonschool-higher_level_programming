#!/usr/bin/python3

"""1-filter_states
Uses the MySQLdb module to search in the database states that start with N
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

    c.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC""")
    result = c.fetchall()

    for i in result:
        print(i)


if __name__ == "__main__":
    db_connection()
