# Import
import pygame
from pygame.locals import *

# defing globals
global zelda_image
global image
image = "voice.gif"
zelda_image = pygame.image.load(image).convert()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Zelda Suck Ass ed.")
# define

class map_update:

    def __init__(self, bg, zelda_pos):
        self.bg = bg
        self.zelda = [zelda_pos[0], zelda_pos[1]]

    def scroll(self):

        self.bg = [self.bg[0], self.bg[1]]

        self.keystate = pygame.key.get_pressed()

        if self.zelda[1] <= 70 and self.bg[1] not in range(-10, 100):
            if self.keystate[pygame.locals.K_UP]:
                self.bg[1] += 5

        if self.zelda[1] >= 505:
            if self.keystate[pygame.locals.K_DOWN]:
                self.bg[1] -= 5

        if self.zelda[0] >= 705:
            if self.keystate[pygame.locals.K_RIGHT]:
                self.bg[0] -= 5

        if self.zelda[0] <= 70 and self.bg[0] not in range(-10, 100):
            if self.keystate[pygame.locals.K_LEFT]:
                self.bg[0] += 5

        return self.bg


class zelda_update:

    def __init__(self, zelda, bg_p):
        self.zelda = [zelda[0], zelda[1]]
        self.bgp = [bg_p[0], bg_p[1]]

    def move(self):

        global zelda_image, image
        self.keystate = pygame.key.get_pressed()

        if self.keystate[pygame.locals.K_DOWN]:

            if image != "voice.gif":
                image = "voice.gif"
                zelda_image = pygame.image.load(image)
                zelda_image = zelda_image.convert()

            if self.zelda[1] <= 505:
                self.zelda[1] += 3

        elif self.keystate[pygame.locals.K_RIGHT]:

            if image != "voice":
                image = "voice.gif"
                zelda_image = pygame.image.load(image)
                zelda_image = zelda_image.convert()

            if self.zelda[0] <= 705:
                self.zelda[0] += 3

        elif self.keystate[pygame.locals.K_UP]:

            if image != "voice.gif":
                image = "voice.gif"
                zelda_image = pygame.image.load(image)
                zelda_image = zelda_image.convert()

            if self.zelda[1] >= 70:
                self.zelda[1] -= 3

        elif self.keystate[pygame.locals.K_LEFT]:

            if image != "voice.gif":
                image = "voice.gif"
                zelda_image = pygame.image.load(image)
                zelda_image = zelda_image.convert()

            if self.zelda[0] >= 70:
                self.zelda[0] -= 3

        self.zelda = (self.zelda[0], self.zelda[1])

        return self.zelda


# set vars out of loop
bg_p = (-10, -10)
zelda_pos = (100, 100)

keepgoing = True

clock = pygame.time.Clock()

# Set up main loop

while keepgoing:

    # time
    clock.tick(30)

    # initiate classes
    zelda = zelda_update(zelda_pos, bg_p)

    map = map_update(bg_p, zelda_pos)

    # Start event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepgoing = False

    # movement
    bg_p = map.scroll()
    zelda_pos = zelda.move()

    # blit images to screen
    screen.blit(background, bg_p)
    screen.blit(zelda_image, zelda_pos)
    pygame.display.flip()
    # end of loop