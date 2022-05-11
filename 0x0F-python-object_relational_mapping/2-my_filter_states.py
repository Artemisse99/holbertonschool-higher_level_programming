#!/usr/bin/python3
"""Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    
    data = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    state = data.cursor()
    state.execute("SELECT * FROM states WHERE name LIKE BINARY '{}%'; "
                .format(sys.argv[4]))
    query_rows = state.fetchall()
    for row in query_rows:
        print(row)
    state.close()
   data.close()
