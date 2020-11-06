import pygame, sys
from settings import Settings

from objects import Player


def tower_master():
    white = [255, 255, 255]
    red = [255, 0, 0]
    pygame.init()
    bg = pygame.image.load("images/background.jpg")

    settings = Settings()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)

    character = Player(screen, settings)

    # Main Game Loop
    while True:
        clock.tick(settings.fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    character.move_left()
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    character.move_right()
                if event.key == pygame.K_SPACE:
                    print('jump')
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    character.move_left(False)
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    character.move_right(False)

        character.update()

        screen.fill(white)
        screen.blit(bg, (0, 0))
        character.blitme()

        pygame.display.flip()


tower_master()
