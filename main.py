import pygame, sys
from settings import Settings

from objects import Player


def tower_master():

    pygame.init()

    settings = Settings()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)

    character = Player(screen, settings)

    # Main Game Loop
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    character.move_left()
                if event.key == pygame.K_RIGHT:
                    character.move_right()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    character.move_left(False)
                elif event.key == pygame.K_RIGHT:
                    character.move_right(False)

        character.update()

        screen.fill((65, 65, 65))
        character.blitme()

        pygame.display.flip()


tower_master()

