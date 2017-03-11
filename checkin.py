import sys
import pygame
import photo

pygame.init()

size = 0, 0

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

screen_width = screen.get_width()
screen_height = screen.get_height()

image_width = int((screen_width - 3) / 5)
image_height = int((screen_height - 3) / 3)

# Blackout the background
colour = 0, 0, 0
screen.fill(colour)
pygame.display.flip()

def handle_keyboard(key):
    if key == pygame.K_ESCAPE:
        sys.exit()

def display_photo(col, row, alpha):
    photo_rect.x = (photo_rect.width + 3) * col
    photo_rect.y = (photo_rect.height + 3) * row
    photo.set_alpha(alpha)
    screen.blit(photo, photo_rect)

# Intialize photos list
photos = []
for i in range(18):
    _photo = photo.Photo(image_width, image_height)
    photos.append(_photo)

# Layout the photos on the screen
i = 0
for x in range(6):
    for y in range(3):
        photos[i].transform(x,y)
        i += 1

i = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            handle_keyboard(event.key)

    screen.fill(colour)
    
    for x in range(18):
        photos[x].setAlpha(i)
        photos[x].drawPhoto(screen)

    pygame.display.flip()
    i += 1
    if i >= 255:
        i = 0
