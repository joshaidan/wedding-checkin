import pygame
import time
import sqlite3
import RPi.GPIO as GPIO
import MFRC522

conn = sqlite3.connect('checkin.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

class CheckIn:

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Helvetica', 50)
        self.table_font = pygame.font.SysFont('Helvetica', 100)
        self.MIFAREReader = MFRC522.MFRC522()

    def check_in(self, user_id):
        """Processing a check in"""
        self.screen.fill((0, 0, 0))

        text = self.font.render('Please wait...', True, (255, 255, 255))
        self.screen.blit(text, (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2)))

        # Look up user_id in database
        c.execute('SELECT * FROM cards INNER JOIN people ON cards.group_id = people.group_id WHERE uuid = ?', (user_id,))
        person = c.fetchone()

        if person is None:
            self.screen.fill((0, 0, 0))
            text = self.font.render("Sorry, we couldn't find you in the database. Please ask for help.", True, (255, 255, 255))
            self.screen.blit(text, (int(self.screen.get_width() / 2 - (text.get_width() / 2)), int(self.screen.get_height() / 2)))
            text = self.font.render(user_id, True, (255, 255, 255))
            self.screen.blit(text, (int(self.screen.get_width() / 2 - (text.get_width() / 2)), int(self.screen.get_height() / 2) + text.get_height()))
        else:
            self.screen.fill((0, 0, 0))
            rectangle = pygame.draw.rect(self.screen, (0, 0, 255), (50, 50, self.screen.get_width() - 100, self.screen.get_height() - 100), 10)

            # text = self.font.render("June 10, 2017", True, (255, 255, 255))
            # self.screen.blit(text, (int(self.screen.get_width() / 2 - (text.get_width() / 2)), 3))

            i = 0
            table_id = person['table_id']
            while person:
                text = self.font.render("%s %s" % (person['firstname'], person['lastname']), True, (255, 255, 255))
                self.screen.blit(text, (int(self.screen.get_width() / 2 - (text.get_width() / 2)), (text.get_height() + 3) * i + 250))
                i += 1
                person = c.fetchone()

            c.execute("SELECT * FROM tables WHERE id = %s" % table_id)
            table = c.fetchone()
            if table:
                table_name = table['name']

                text = self.table_font.render("%s" % table_name, True, (255, 255, 255))
                self.screen.blit(text, (int(self.screen.get_width() / 2 - (text.get_width() / 2)), (text.get_height() + 3) * 5))

        pygame.display.flip()
        time.sleep(10)

    def watch_check_in(self):
        # Scan for a card
        (status, TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)

        if status == self.MIFAREReader.MI_OK:
            # Card found
            (status, uid) = self.MIFAREReader.MFRC522_Anticoll()
            if status == self.MIFAREReader.MI_OK:
                card_id = str(uid[0]) + '-' + str(uid[1]) + '-' + str(uid[2]) + '-' + str(uid[3])
                self.check_in(card_id)
