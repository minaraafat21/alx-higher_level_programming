#!/usr/bin/python3
"""Deletes duplicate states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    
    # Execute a query to delete duplicate rows
    cur.execute("""
        DELETE FROM states 
        WHERE id NOT IN (
            SELECT MIN(id) 
            FROM states 
            GROUP BY name
        )
    """)
    
    # Commit the changes to the database
    conn.commit()
    
    cur.close()
    conn.close()
