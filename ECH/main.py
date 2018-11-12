import pygame
pygame.init()

DISPLAY_WIDTH = 1024
DISPLAY_HEIGHT = 720
DISPLAY_TITLE = 'Demo'
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
PERSON_IMAGE = pygame.image.load('Person.png')
PERSON_IMAGE_WIDTH = 71
PERSON_IMAGE_HEIGHT = 127


gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(DISPLAY_TITLE)
clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            print(event)

    pygame.display.update()
    clock.tick(10)

pygame.quit()
quit()