#!/usr/bin/python3
"""lists all states from the
database hbtn_0e_0_usa"""
import MySQLdb
import sys 

if __name__ == "__main__":

    data = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    state = data.cursor()
    state.execute("SELECT * FROM states WHERE name = \
                %s ORDER BY states.id ASC", (argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    state.close()
    data.close()