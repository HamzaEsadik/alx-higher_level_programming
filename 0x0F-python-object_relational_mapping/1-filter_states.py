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

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY "
                "name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
