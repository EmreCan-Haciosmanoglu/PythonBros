import pygame
pygame.init()

CLOCK_TICK = 60
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
PERSON_JUMP_SPEED = -200
PERSON_WALKING_SPEED = 180
MAGNITUDE_OF_ACCELERATION_CAUSED_BY_FRICTION = 100
ACCELERATION_CAUSED_BY_GRAVITY = 100


gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(DISPLAY_TITLE)
clock = pygame.time.Clock()

crashed = False
getTicksLastFrame = 0
deltaTime = 0


def physics():
    global PERSON_POSITION_X
    global PERSON_POSITION_Y
    global PERSON_VELOCITY_X
    global PERSON_VELOCITY_Y

    PERSON_POSITION_Y += PERSON_VELOCITY_Y * deltaTime
    PERSON_POSITION_X += PERSON_VELOCITY_X * deltaTime
    if PERSON_VELOCITY_X > 0 and PERSON_VELOCITY_X > MAGNITUDE_OF_ACCELERATION_CAUSED_BY_FRICTION:
        PERSON_VELOCITY_X -= MAGNITUDE_OF_ACCELERATION_CAUSED_BY_FRICTION * deltaTime
    elif PERSON_VELOCITY_X < 0 and -PERSON_VELOCITY_X > MAGNITUDE_OF_ACCELERATION_CAUSED_BY_FRICTION:
        PERSON_VELOCITY_X += MAGNITUDE_OF_ACCELERATION_CAUSED_BY_FRICTION * deltaTime
    else:
        PERSON_VELOCITY_X = 0

    if PERSON_POSITION_Y >= DISPLAY_HEIGHT - PERSON_IMAGE_HEIGHT - GROUND_HEIGHT:
        PERSON_POSITION_Y = DISPLAY_HEIGHT - PERSON_IMAGE_HEIGHT - GROUND_HEIGHT
        PERSON_VELOCITY_Y = 0
    else:
        PERSON_VELOCITY_Y += ACCELERATION_CAUSED_BY_GRAVITY * deltaTime

    if PERSON_POSITION_X <= 0:
        PERSON_VELOCITY_X = 0
        PERSON_POSITION_X = 0
    elif PERSON_POSITION_X >= DISPLAY_WIDTH - PERSON_IMAGE_WIDTH:
        PERSON_VELOCITY_X = 0
        PERSON_POSITION_X = DISPLAY_WIDTH - PERSON_IMAGE_WIDTH
    else:
        PERSON_POSITION_X += PERSON_VELOCITY_X * deltaTime


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
            if event.key == pygame.K_LEFT:
                PERSON_VELOCITY_X = -PERSON_WALKING_SPEED
            if event.key == pygame.K_RIGHT:
                PERSON_VELOCITY_X = PERSON_WALKING_SPEED

    physics()
    gameDisplay.fill(COLOR_WHITE)
    person(PERSON_POSITION_X, PERSON_POSITION_Y)

    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    pygame.display.update()
    clock.tick(CLOCK_TICK)

pygame.quit()
quit()
