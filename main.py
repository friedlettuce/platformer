import pygame_menu
import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf
from objects import Player, Skeleton, Level, Platform, Exit_Ladder
import objects



def tower_master():

    settings = Settings()
    clock = pygame.time.Clock()
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)
    bg = pygame.image.load(settings.background_img)

    level = Level()

    character = Player(screen, settings)
    exit = Exit_Ladder(settings.screen_width / 2, (settings.screen_height / 2) + 56)

    # group to store throwing knives
    knives = Group()
    platforms = objects.plat_list
    floor = objects.ground_list
    enemies = level.bad(1, screen, settings)

    # Main Game Loop
    while True:
        clock.tick(settings.fps)
        gf.check_events(settings, screen, character, knives, knifeSound)

        character.update()
        character.gravity()
        gf.update_enemies(character, enemies, hitSound)

        gf.update_knives(knives, enemies)

        gf.update_screen(settings, screen, character, bg, knives, platforms, enemies, floor, exit)
        gf.check_win(character, exit)

pygame.init()

knifeSound = pygame.mixer.Sound('sounds/throw.wav')
hitSound = pygame.mixer.Sound('sounds/ouch.wav')

music = pygame.mixer.music.load('sounds/levelMusic.wav')
surface = pygame.display.set_mode((600, 400))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    tower_master()
    pass


menu = pygame_menu.Menu(300, 400, 'Tower Master v0.0.1',
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add_text_input('Please enter name:', default='Hero')
menu.add_selector('Level Selector :', [('Level 1', 1), ('Level 2', 2)], onchange=set_difficulty)
menu.add_button('Start Game', start_the_game)
menu.add_button('Exit Game', pygame_menu.events.EXIT)
surface = pygame.display.set_mode((600, 400))

menu.mainloop(surface)

start_the_game()
