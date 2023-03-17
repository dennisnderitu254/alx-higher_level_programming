#!/usr/bin/env python3
# Lists all states with a name starting with N from the database hbtn_0e_0_usa.
# Usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>

import sys
import MySQLdb

if __name__ == '__main__':
    # Check for the correct number of arguments
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} username password database")
        sys.exit(1)

    # Connect to MySQL database
    try:
        db = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    except MySQLdb.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

    # Execute the SQL query
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")

    # Fetch and display the results
    [print(state) for state in c.fetchall() if state[1][0] == "N"]

    # Close the cursor and connection
    c.close()
    db.close()
