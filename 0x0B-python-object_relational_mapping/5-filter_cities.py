#!/usr/bin/python3
"""lists all cities in a given state"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities JOIN states ON \
            cities.state_id = states.id WHERE states.name \
                LIKE BINARY %(k)s GROUP BY cities.name", {'k': argv[4]}
    )
    cities = cur.fetchall()
    if cities is not None:
        print(", ".join(city[0] for city in cities))
    cur.close()
    db.close()
