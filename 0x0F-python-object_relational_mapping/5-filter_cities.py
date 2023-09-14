#!/usr/bin/python3
"""
Takes in the name of a state
as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.
"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor() # creates a cursor
    cursor.execute("SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s, (sys.argv[4],)") # fetch states sorted by states.id
    states = cursor.fetchall() # fetches all rows
    for row in states:
        print(row)
        cursor.close() # close all cursors
        db.close() # close all database
