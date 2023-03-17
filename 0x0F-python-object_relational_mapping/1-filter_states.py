#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == '__main__':
    # Check for the correct number of arguments
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} username password database")
        sys.exit(1)

    # Connect to MySQL database
    try:
        conn = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    except MySQLdb.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

    # Execute the SQL query
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and display the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()
