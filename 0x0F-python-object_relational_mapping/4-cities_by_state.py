#!/usr/bin/python3
"""  
lists all cities from
the database `hbtn_0e_4_usa`.
"""
import MySQLdb
import sys

"""
Accessing the database in order
to get the cities.
"""


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = db.cursor()
    mycursor.execute("""SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id=cities.state_id""")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    db.close()
