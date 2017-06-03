import csv
import sys
import sqlite3

conn = sqlite3.connect('checkin.db')
# conn.row_factory = sqlite3.Row
c = conn.cursor()

tables = []

f = open('guests.csv', 'r')
reader = csv.reader(f)

for row in reader:
    table_name = row[3]
    if not table_name in tables:
        tables.append(table_name)

i = 1
for table in tables:
    query = "INSERT INTO tables (id, name) VALUES (?, ?)"
    c.execute(query, (i, table))
    i += 1

f.seek(0)

uid = 1
for row in reader:
    group_id = row[0]
    firstname = row[1]
    lastname = row[2]
    table_name = row[3]
    comment = row[4]
    table_id = tables.index(table_name) + 1

    query = "INSERT INTO people (id, firstname, lastname, group_id, table_id) VALUES (?, ?, ?, ?, ?)"
    c.execute(query, (uid, firstname, lastname, group_id, table_id))
    uid += 1

conn.commit()
conn.close()

f.close()
