#!/usr/bin/python3
"get states"
from sys import argv
import MySQLdb


def main():
    user = sys.argv[1]
    ps = sys.argv[2]
    dbn = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=ps, db=dbn, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    mylist = cur.fetchall()
    for row in mylist:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
