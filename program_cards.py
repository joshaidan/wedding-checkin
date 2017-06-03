import sqlite3
import RPi.GPIO as GPIO
import MFRC522
import time

MIFAREReader = MFRC522.MFRC522()

def listen_for_card():
    while True:
        # Scan for a card
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        if status == MIFAREReader.MI_OK:
            # Card found
            (status, uid) = MIFAREReader.MFRC522_Anticoll()
            if status == MIFAREReader.MI_OK:
                card_id = str(uid[0]) + '-' + str(uid[1]) + '-' + str(uid[2]) + '-' + str(uid[3])
                if not card_id in card_cache:
                    return card_id

conn = sqlite3.connect('checkin.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()
insert = conn.cursor()

card_cache = []

c.execute("SELECT group_id, firstname, lastname FROM people WHERE group_id NOT IN (SELECT group_id FROM cards) GROUP BY group_id")


rows = c.fetchall()

for row in rows:
    group_id = row['group_id']
    firstname = row['firstname']
    lastname = row['lastname']

    # if (firstname == 'Jeff' and lastname == 'Jones') or firstname == 'Jeffrey':
    #     continue

    # if firstname in ['Jeff', 'Jeffrey', 'Jennifer'] and lastname in ['Jones', 'Boschman', 'Anderson']:
    #     continue

    print("Programming card for %s %s" % (firstname, lastname))
    card_id = listen_for_card()

    print("CARD ID: %s" % card_id)
    card_cache.append(card_id)

    insert.execute('INSERT INTO cards (uuid, group_id) VALUES (?, ?)', (card_id, group_id))
    conn.commit()

    time.sleep(1)


conn.close()
   
