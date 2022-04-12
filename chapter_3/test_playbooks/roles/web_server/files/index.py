#!/usr/bin/python3

import pymysql

# Print necessary headers.
print("Content-Type: text/html")
print()

# Connect to the database.
conn = pymysql.connect(
            db='testdb',
            user='root',
            passwd='password',
            host='localhost')
c = conn.cursor()

# Print the contents of the table.
c.execute("SELECT * FROM test;")
for i in c:
    print(i)
