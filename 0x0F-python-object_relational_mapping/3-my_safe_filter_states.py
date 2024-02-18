#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3], charset="utf8")
        cur = conn.cursor()

        # Use a parameterized query
        sql = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC"
        cur.execute(sql, (argv[4],))

        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        cur.close()
        conn.close()
