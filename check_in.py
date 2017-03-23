import pygame
import time
import sqlite3

conn = sqlite3.connect('checkin.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

class CheckIn:

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Helvetica', 30)

    def check_in(self, user_id):
        """Processing a check in"""
        self.screen.fill((0,0,0))

        text = self.font.render('Please wait...', False, (255,255,255))
        self.screen.blit(text, (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2)))

        # Look up user_id in database
        c.execute('SELECT * FROM people WHERE uuid = ?', (user_id,))
        person = c.fetchone()
        if not person:
            self.screen.fill((0,0,0))
            text = self.font.render("Sorry, we couldn't find you in the database. Please ask for help.", False, (255,255,255))
            self.screen.blit(text, (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2)))
        else:
            self.screen.fill((0,0,0))
            text = self.font.render("Hi %s!" % person['firstname'], False, (255,255,255))
            self.screen.blit(text, (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2)))

        pygame.display.flip()
        time.sleep(5)