#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
with a `name` starting with the letter `N`
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Accessing the database in order
    to get the states.
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = db.cursor() # create a cursor
    mycursor.execute("SELECT * FROM states  WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    db.close()
