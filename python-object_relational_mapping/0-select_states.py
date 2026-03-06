# #!/usr/bin/python3

"""0-select_states
Uses the MySQLdb module to interact with a database using Python
"""

import MySQLdb
from sys import argv


def db_connection():
    """Connects to the database and fetches all rows from the states table"""

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], password=argv[2], database=argv[3]
    )
    c = db.cursor()

    c.execute("""SELECT * FROM states""")
    result = c.fetchall()

    for i in result:
        print(i)


if __name__ == "__main__":
    db_connection()
