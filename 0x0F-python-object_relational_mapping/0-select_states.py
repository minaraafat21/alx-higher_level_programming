#!/usr/bin/python3

"""
This script lists all the states from the 'states' table in a MySQL database.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the MySQL database
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()

    # Execute the SQL query to select all the states
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all the rows returned by the query
    query_rows = cur.fetchall()

    # Print each row
    for row in query_rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    conn.close()
