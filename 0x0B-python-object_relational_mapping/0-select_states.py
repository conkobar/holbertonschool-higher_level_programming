#!/usr/bin/python3
"""script to list all states from db"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """this is the script"""
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    records = c.fetchall()
    for record in records:
        print(record)
