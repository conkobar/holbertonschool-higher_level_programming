#!/usr/bin/python3
"""displays all values in states table that match arg"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(
        user=argv[1], passwd=argv[2], db=argv[3]
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id"
        .format(argv[4])
    )
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
