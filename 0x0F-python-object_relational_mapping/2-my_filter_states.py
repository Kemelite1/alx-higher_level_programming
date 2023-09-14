#!/usr/bin/python3
"""
displays all values in the states table of 'hbtn_0e_0_usa'
where the name matches the argument provided.
"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor() # creates a cursor
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC") # fetch states sorted by states.id
    states = cursor.fetchall() # fetches all rows
    for row in states:
        print(row)
        cursor.close() # close all cursors
        db.close() # close all databases
