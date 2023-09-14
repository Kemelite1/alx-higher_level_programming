#!/usr/bin/python3
"""
Takes in arguments, and displays all values in the 'states' table of 'hbtn_0e_0_usa'
where the 'name' matches the argument safely.
"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor() # creates a cursor
    match = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match, )") # fetch states sorted by states.id
    states = cursor.fetchall() # fetches all rows
    for row in states:
        print(row)
        cursor.close() # close all cursors
        db.close() # close all databases
