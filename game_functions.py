import sys

import pygame
import objects
from objects import Knife

def check_events(settings, screen, character, knives, platforms, enemies):
    # check for keypresses and other events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, character, knives, settings, screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, character)

def check_keydown_events(event, character, knives, settings, screen):
    # this function deals with any keydown event
    if event.key == pygame.K_LEFT or event.key == ord('a'):
        character.move_left()
    if event.key == pygame.K_RIGHT or event.key == ord('d'):
        character.move_right()
    if event.key == pygame.K_SPACE:
        character.jump()
    if event.key == pygame.K_f or event.key == ord('f'):
        if character.flipped:
            character.attack_l_state()
        else:
            character.attack_r_state()
    if event.key == pygame.K_g:
        throw_knife(settings, screen, character, knives, character.flipped)

def check_keyup_events(event, character):
    # this function deals with any keyup event
    if event.key == pygame.K_LEFT or event.key == ord('a'):
        character.move_left(False)
    elif event.key == pygame.K_RIGHT or event.key == ord('d'):
        character.move_right(False)

def update_screen(settings, screen, character, bg, skeleton, knives, platforms, enemies):
    # this is where the screen is updated
    screen.fill(settings.white)
    screen.blit(bg, (0, 0))
    skeleton.blitme()
    character.blitme()
    # redraw all knives
    for knife in knives.sprites():
        knife.draw_knife()
    pygame.display.flip()

def update_knives(knives, skeleton):
    # update positions of knives and delete off screen ones
    knives.update()

    # delete off screen knives
    for knife in knives.copy():
        # if it goes off screen
        if knife.rect.right <= 0 or knife.rect.left >= 1000:
            knives.remove(knife)
        # if it hits an enemy
        if skeleton.hitbox[1] + skeleton.hitbox[3] > knife.y > skeleton.hitbox[1]:
            if skeleton.hitbox[0] < knife.x < skeleton.hitbox[0] + skeleton.hitbox[2]:
                skeleton.hit_knife()
                knives.remove(knife)

def throw_knife(settings, screen, character, knives, flipped):
    # create a new bullet if there isn't 3 currently on screen
    if len(knives) < settings.knives_allowed:
        new_knife = Knife(settings, screen, character, flipped)
        knives.add(new_knife)


