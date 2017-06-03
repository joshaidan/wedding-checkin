import sqlite3

conn = sqlite3.connect('checkin.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

c.execute("SELECT group_id, firstname, lastname FROM people")

row = c.fetchone()
last_group_id = row['group_id']

while row:
    print("%s %s" % (row['firstname'], row['lastname']))

    row = c.fetchone()
    if row and row['group_id'] != last_group_id:
        last_group_id = row['group_id']
        print("")