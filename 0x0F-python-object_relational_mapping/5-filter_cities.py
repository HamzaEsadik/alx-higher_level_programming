#!/usr/bin/python3
'''first module'''
import MySQLdb
import sys


def main():
    '''this is the main function'''
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
        )

    qr = "SELECT cities.name FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s ORDER BY cities.id"
    vr = (sys.argv[4], )
    cur = db.cursor()
    cur.execute(qr, vr)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
