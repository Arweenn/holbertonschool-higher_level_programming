#!/usr/bin/python3

from sys import argv
import MySQLdb


if __name__ == '__main__':
   # if len(argv) != 4:
    #    print("Usage: {} <username> <password> <database>".format(argv[0]))
     #   exit(1)

    conn = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
