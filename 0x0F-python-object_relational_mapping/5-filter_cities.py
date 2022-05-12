#!/usr/bin/python3
"""lists all states from the
database hbtn_0e_0_usa"""


if __name__ == "__main__":

    import MySQLdb
    import sys

    data = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])

    state = data.cursor()
    state.execute("SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name=%s ORDER BY cities.id ASC", (sys.argv[4], ))

    query_rows = state.fetchall()
    sig = ""
    for row in query_rows:
        print("{}{}".format(sig, row[0]), end="")
        sig = ", "
    print()

    state.close()
    data.close()
