import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf
from objects import Player, Skeleton


def tower_master():

    pygame.init()

    settings = Settings()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)
    bg = pygame.image.load(settings.background_img)

    character = Player(screen, settings)
    skeleton = Skeleton(screen, settings)

    # group to store throwing knives
    knives = Group()
    platforms = Group()
    enemies = Group()

    # Main Game Loop
    while True:
        clock.tick(settings.fps)

        gf.check_events(settings, screen, character, knives, platforms, enemies)

        character.update()
        character.gravity()
        skeleton.update()

        gf.update_knives(knives, skeleton)

        gf.update_screen(settings, screen, character, bg, skeleton, knives, platforms, enemies)


tower_master()
