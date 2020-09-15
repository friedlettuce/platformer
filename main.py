import sys
import pygame
from settings import Settings


def tower_master():

    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)

    # Main Game Loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


tower_master()

