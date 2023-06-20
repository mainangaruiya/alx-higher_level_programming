#!/usr/bin/env python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the query to fetch cities with their respective states
    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "ORDER BY cities.id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
