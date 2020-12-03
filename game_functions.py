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
    if event.key == pygame.K_LSHIFT:
        if character.flipped:
            character.dash_l_state()
        else:
            character.dash_r_state()
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
    if event.key == pygame.K_LSHIFT:
        if character.flipped:
            character.move_left(False)
        else:
            character.move_right(False)

def update_screen(settings, screen, character, bg, knives, platforms, enemies, floor, exit):
    # this is where the screen is updated
    screen.fill(settings.white)
    screen.blit(bg, (0, 0))
    # draw all ground
    for ground in floor.copy():
        screen.blit(ground.image, ground.rect)
    # draw all platforms
    for platform in platforms.sprites():
        screen.blit(platform.image, platform.rect)
    # draw the exit ladder
    screen.blit(exit.image, exit.rect)
    character.blitme()
    # redraw all knives
    for knife in knives.sprites():
        knife.draw_knife()
    # redraw all enemies
    for enemy in enemies.copy():
        enemy.blitme()
    pygame.display.flip()

def update_knives(knives, enemies):
    # update positions of knives and delete off screen ones
    knives.update()

    # delete off screen knives
    for knife in knives.copy():
        # if it goes off screen
        if knife.rect.right <= 0 or knife.rect.left >= 1000:
            knives.remove(knife)
        # if it hits an enemy
        for enemy in enemies.copy():
            if enemy.hitbox[1] + enemy.hitbox[3] > knife.y > enemy.hitbox[1]:
                if enemy.hitbox[0] < knife.x < enemy.hitbox[0] + enemy.hitbox[2]:
                    enemy.hit_knife()
                    knives.remove(knife)

def throw_knife(settings, screen, character, knives, flipped):
    # create a new bullet if there isn't 3 currently on screen
    if len(knives) < settings.knives_allowed:
        new_knife = Knife(settings, screen, character, flipped)
        knives.add(new_knife)

def update_enemies(character, enemies):
    for enemy in enemies.copy():
        enemy.update()
        if character.hitbox.colliderect(enemy.hitbox):
            character.hit()
        if enemy.hitbox.colliderect(character.sword_hitbox):
            enemy.hit_sword()
        if enemy.health <= 0:
            enemies.remove(enemy)

def check_win(character, exit):
    if character.hitbox[1] + character.hitbox[3] > exit.rect.centery > character.hitbox[1]:
        if character.hitbox[0] < exit.rect.centerx < character.hitbox[0] + character.hitbox[2]:
            print("You beat the level!")
            sys.exit()
