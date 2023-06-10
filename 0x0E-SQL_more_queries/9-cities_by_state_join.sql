#!/bin/bash

# Get the database name from the command line argument
database_name="$1"

# MySQL command to execute the SELECT statement
mysql_command="SELECT cities.id, cities.name, states.name
               FROM cities
               INNER JOIN states ON cities.state_id = states.id
               ORDER BY cities.id ASC;"
