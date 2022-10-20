#!/usr/bin/python3
"""lists all cities in database"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities JOIN states \
            ON cities.state_id = states.id ORDER BY cities.id"
    )
    for city in cur.fetchall():
        print(city)
    db.close()
    cur.close()
