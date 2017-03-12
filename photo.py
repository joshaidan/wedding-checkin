import pygame
import random

NUM_PHOTOS = 3

class Photo:
    """Photo is a photo displayed in the check-in system"""

    alpha = 255
    fading = False

    def __init__(self, width, height):
        num = random.randint(1, NUM_PHOTOS)
        self.width = width
        self.height = height
        self.set_photo("media/photo" + str(num) + ".png", self.width, self.height)
        self.rect = self.photo.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.old_photo = self.photo

    def transform(self, col, row):
        self.rect.x = (self.rect.width + 3) * col
        self.rect.y = (self.rect.height + 3) * row
    
    def draw_photo(self, screen):
        self.set_alpha()
        screen.blit(self.old_photo, self.rect)
        screen.blit(self.photo, self.rect)

    def set_alpha(self):
        self.photo.set_alpha(self.alpha)

    def set_photo(self, filename, width, height):
        self.photo = pygame.image.load(filename).convert()
        self.photo = pygame.transform.scale(self.photo, (width, height))

    def fade_in(self):
        self.fading = True
        self.alpha = 0

    def change_photo(self):
        if not self.fading:
            self.old_photo = self.photo
            num = random.randint(1, NUM_PHOTOS)
            self.set_photo("media/photo" + str(num) + ".png", self.width, self.height)
            self.fade_in()

    def tick(self, screen):
        if self.fading:
            self.alpha += 1
            if self.alpha >= 255:
                self.fading = False
        elif random.randint(0,100) == 50:
            self.change_photo()
        
        self.draw_photo(screen)
