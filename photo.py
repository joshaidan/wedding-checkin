import pygame

class Photo:
    """Photo is a photo displayed in the check-in system"""

    def __init__(self, width, height):
        self.photo = pygame.image.load("media/photo1.bmp").convert()
        self.photo = pygame.transform.scale(self.photo, (width, height))
        self.rect = self.photo.get_rect()

        self.rect.x = 0
        self.rect.y = 0
        self.photo.set_alpha(128)

    def transform(self, col, row):
        self.rect.x = (self.rect.width + 3) * col
        self.rect.y = (self.rect.height + 3) * row
    
    def drawPhoto(self, screen):
        screen.blit(self.photo, self.rect)

    def setAlpha(self, alpha):
        self.photo.set_alpha(alpha)