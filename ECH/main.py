import pygame
pygame.init()

DISPLAY_WIDTH = 1024
DISPLAY_HEIGHT = 720
GROUND_HEIGHT = 10
DISPLAY_TITLE = 'Demo'
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
PERSON_IMAGE = pygame.image.load('Person.png')
PERSON_IMAGE_WIDTH = 71
PERSON_IMAGE_HEIGHT = 127
PERSON_POSITION_X = DISPLAY_WIDTH * 0.25 - PERSON_IMAGE_WIDTH
PERSON_POSITION_Y = DISPLAY_HEIGHT - PERSON_IMAGE_HEIGHT - GROUND_HEIGHT
PERSON_VELOCITY_X = 0
PERSON_VELOCITY_Y = 0
PERSON_JUMP_SPEED = -40
GRAVITY = 5


gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(DISPLAY_TITLE)
clock = pygame.time.Clock()

crashed = False


def physics():
    global PERSON_VELOCITY_Y
    global PERSON_POSITION_Y
    PERSON_POSITION_Y += PERSON_VELOCITY_Y
    if PERSON_POSITION_Y == DISPLAY_HEIGHT - PERSON_IMAGE_HEIGHT - GROUND_HEIGHT:
        PERSON_VELOCITY_Y = 0
    elif PERSON_POSITION_Y > DISPLAY_HEIGHT - PERSON_IMAGE_HEIGHT - GROUND_HEIGHT:
        PERSON_POSITION_Y = DISPLAY_HEIGHT - PERSON_IMAGE_HEIGHT - GROUND_HEIGHT
        PERSON_VELOCITY_Y = 0
    else:
        PERSON_VELOCITY_Y += GRAVITY


def person(x, y):
    gameDisplay.blit(PERSON_IMAGE, (x, y))


while not crashed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and PERSON_POSITION_Y == DISPLAY_HEIGHT - PERSON_IMAGE_HEIGHT - GROUND_HEIGHT:
                print(event)
                PERSON_VELOCITY_Y = PERSON_JUMP_SPEED
    physics()
    gameDisplay.fill(COLOR_WHITE)
    person(PERSON_POSITION_X, PERSON_POSITION_Y)

    pygame.display.update()
    clock.tick(10)

pygame.quit()
quit()