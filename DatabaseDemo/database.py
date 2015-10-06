#!/usr/bin/python

# Use the following directive to import the MySQL libraries.
import MySQLdb

# Creates a MySQLdb instance, use appropriate parameters depending on server.
db = MySQLdb.connect(host = "localhost", user = "USERNAME", passwd ="PASSWORD", db = "address_book")

# Creates a cursor object that allows you to perform all SQL transactions.
cur = db.cursor()

# Execute SQL commands as follows.
cur.execute("SELECT * FROM people")

# Check to see how many records are there in the query result.
#print len(cur.fetchall())

# Sample methods to iterate through data
# Here, we print the second and third column for each row
# (essentially the first and last name)
for row in cur.fetchall():
    print str(row[1]) + " " + str(row[2])
    # Must wrap around str to change to string so we can append a space in between.
