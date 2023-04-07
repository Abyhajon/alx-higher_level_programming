#!/usr/bin/python3
"""
ists all values in the states tables of a database where name
matches the argument.
"""
import sys
import MySQLdb

# Get the command line arguments
mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
db_name = sys.argv[3]
state_name = sys.argv[4]

# Connect to the MySQL server
db = MySQLdb.connect(user=mysql_user, passwd=mysql_password, db=db_name, host="localhost", port=3306)

# Create a cursor object
cursor = db.cursor()

# Construct the SELECT statement with user input
query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)

# Execute the SELECT statement
cursor.execute(query)

# Fetch all the rows returned by the SELECT statement
rows = cursor.fetchall()

# Print the rows in the required format
for row in rows:
    print(row)

# Close the cursor and connection objects
cursor.close()
db.close()
