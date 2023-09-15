#!/usr/bin/python3
"""
displays all values in the states table of 'hbtn_0e_0_usa'
where the name matches the argument provided.
"""

import MySQLdb
import sys

"""
Accessing the database in order
to get the states.
"""

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = db.cursor() 
    mycursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4]))
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    db.close()
