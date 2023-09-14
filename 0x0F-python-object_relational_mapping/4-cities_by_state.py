#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor() # creates a cursor
    cursor.execute("SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id") # fetch states sorted by states.id
    states = cursor.fetchall() # fetches all rows
    for row in states:
        print(row)
        cursor.close() # close all cursors
        db.close() # close all databases
