#!/usr/bin/python3
import sys
import MySQLdb
def main():
    user = sys.argv[1]
    ps = sys.argv[2]
    dbn = sys.argv[3]
    db = MySQLdb.connect(host='localhost', user=user,
                         passwd=ps, db=dbn, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
