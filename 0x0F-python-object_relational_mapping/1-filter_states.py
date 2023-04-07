#!/usr/bin/python3
"""
Lists all states with a name starting with N
"""
import MySQLdb
import sys

if __name__ == '__main__':
    
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()

