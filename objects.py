import pygame
from pygame.sprite import Sprite
from enum import Enum
import settings
import os
#Guide used to implement jump and platform mechanics
#https://opensource.com/article/19/12/jumping-python-platformer-game
#https://opensource.com/article/18/7/put-platforms-python-game
#This is a change
worldx = 960
worldy = 720
fps = 40
ani = 4
BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)


class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'brick_platform' + '.png'))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc



class Object:

    def __init__(self, screen, info):
        self.screen = screen
        self.curr_image = None
        self.rect = None
        self.curr_frame = 0
        self.frame_count = 0

        self.info = info
        self.sprite_sheet = pygame.image.load(self.info['location'])

    def inc_frame(self):
        self.curr_frame = (self.curr_frame + 1) % self.frame_count

    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), rect)
        return image

    def blitme(self):
        self.screen.blit(self.curr_image, self.rect)


class State(Enum):
    IDLE = 0
    WALK = 1
    ATTACK = 2
    JUMP = 3


class Character(Object):

    def __init__(self, screen, sprite_info):
        super().__init__(screen, sprite_info)

        self.state = None
        self.flipped = False
        self.moving_right = False
        self.moving_left = False

        self.idle_r_frames = []

        rx_pos = self.info['idle_rx_starts']
        ry_pos = self.info['idle_ry_starts']
        for frame in range(self.info['idle_frames']):
            self.idle_r_frames.append(self.image_at((rx_pos[frame], ry_pos[frame],
                                                     self.info['size'][0], self.info['size'][1])))
        # Points to which array of frames to use
        self.curr_frames = None

    def move_left(self, flag=True):
        if flag and self.state is not State.WALK:
            self.walk_l_state()
        elif not self.moving_right and self.state is not State.IDLE:
            self.idle_l_state()
        self.moving_left = flag
        self.flipped = flag

    def move_right(self, flag=True):
        if flag and self.state is not State.WALK:
            self.walk_r_state()
        elif not self.moving_left and self.state is not State.IDLE:
            self.idle_r_state()
        self.moving_right = flag
        self.flipped = False

    def idle_r_state(self):
        self.state = State.IDLE
        self.curr_frame = 0
        self.frame_count = self.info['idle_frames']
        self.curr_frames = self.idle_r_frames

    def idle_l_state(self):
        self.state = State.IDLE
        self.curr_frame = 0
        self.frame_count = self.info['idle_frames']
        self.curr_frames = self.idle_l_frames

    def walk_r_state(self):
        if self.state is State.ATTACK:
            return
        self.state = State.WALK
        self.curr_frame = 0
        self.frame_count = self.info['walk_frames']
        self.curr_frames = self.walk_r_frames

    def walk_l_state(self):
        self.state = State.IDLE
        self.curr_frame = 0
        self.frame_count = self.info['walk_frames']
        self.curr_frames = self.walk_l_frames

    def attack_r_state(self):
        if self.state == State.ATTACK:
            return
        self.state = State.ATTACK
        self.curr_frame = 0
        self.frame_count = self.info['attack_frames']
        self.curr_frames = self.attack_r_frames

    def attack_l_state(self):
        if self.state == State.ATTACK:
            return
        self.state = State.ATTACK
        self.curr_frame = 0
        self.frame_count = self.info['attack_frames']
        self.curr_frames = self.attack_l_frames


class Player(Character):

    def __init__(self, screen, settings):
        self.movex = 0
        self.movey = 0
        super().__init__(screen, settings.player_sprite)

        self.walking_speed = settings.player_w_speed
        self.is_jumping = True
        self.is_falling = False
        self.rect = self.idle_r_frames[0].get_rect()
        self.rect.centerx = self.info['start_pos'][0]
        self.rect.bottom = self.info['start_pos'][1]

        self.idle_l_frames = []
        self.walk_r_frames = []
        self.walk_l_frames = []
        self.attack_r_frames = []
        self.attack_l_frames = []
        self.jump_r_frames = []
        self.jump_l_frames = []

        # set up animation arrays
        lx_pos = self.info['idle_lx_starts']
        ly_pos = self.info['idle_ly_starts']
        for frame in range(self.info['idle_frames']):
            self.idle_l_frames.append(self.image_at((lx_pos[frame], ly_pos[frame],
                                                    self.info['size'][0], self.info['size'][1])))
        rx_pos = self.info['walk_rx_starts']
        ry_pos = self.info['walk_ry_starts']
        for frame in range(self.info['walk_frames']):
            self.walk_r_frames.append(self.image_at((rx_pos[frame], ry_pos[frame],
                                                   self.info['size'][0], self.info['size'][1])))
        lx_pos = self.info['walk_lx_starts']
        ly_pos = self.info['walk_ly_starts']
        for frame in range(self.info['walk_frames']):
            self.walk_l_frames.append(self.image_at((lx_pos[frame], ly_pos[frame],
                                                    self.info['size'][0], self.info['size'][1])))
        rx_pos = self.info['attack_rx_starts']
        ry_pos = self.info['attack_ry_starts']
        for frame in range(self.info['attack_frames']):
            self.attack_r_frames.append(self.image_at((rx_pos[frame], ry_pos[frame],
                                                     self.info['size'][0], self.info['size'][1])))
        lx_pos = self.info['attack_lx_starts']
        ly_pos = self.info['attack_ly_starts']
        for frame in range(self.info['attack_frames']):
            self.attack_l_frames.append(self.image_at((lx_pos[frame], ly_pos[frame],
                                                      self.info['size'][0], self.info['size'][1])))
        rx_pos = self.info['jump_rx_starts']
        ry_pos = self.info['jump_ry_starts']
        for frame in range(self.info['jump_frames']):
            self.jump_r_frames.append(self.image_at((rx_pos[frame], ry_pos[frame],
                                                   self.info['size'][0], self.info['size'][1])))
        lx_pos = self.info['jump_lx_starts']
        ly_pos = self.info['jump_ly_starts']
        for frame in range(self.info['jump_frames']):
            self.jump_l_frames.append(self.image_at((lx_pos[frame], ly_pos[frame],
                                                    self.info['size'][0], self.info['size'][1])))
        self.idle_r_state()

    def gravity(self):
        if self.is_jumping:
            self.movey += 2   #Edit this value to change jump height

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x

    def jump(self):
        if self.is_jumping is False:
            self.is_falling = False
            self.is_jumping = True

    def update(self):

        if self.moving_right:
            self.rect.centerx += self.walking_speed
        elif self.moving_left:
            self.rect.centerx -= self.walking_speed

        if self.state is State.ATTACK and self.curr_frame + 1 is self.info['attack_frames']:
            self.idle_r_state()
        else:
            self.inc_frame()

        self.curr_image = self.curr_frames[self.curr_frame]

        if self.movex < 0:
            self.is_jumping = True
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

            # moving right
        if self.movex > 0:
            self.is_jumping = True
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]

            # collisions
        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        #for enemy in enemy_hit_list:
            #self.health -= 1
            # print(self.health)

        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
        for g in ground_hit_list:
            self.movey = 0
            self.rect.bottom = g.rect.top
            self.is_jumping = False  # stop jumping

        # fall off the world
        if self.rect.y > worldy:
            self.health -= 1
            print(self.health)
            self.rect.x = tx
            self.rect.y = ty

        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        for p in plat_hit_list:
            self.is_jumping = False  # stop jumping
            self.movey = 0
            if self.rect.bottom <= p.rect.bottom:
                self.rect.bottom = p.rect.top
            else:
                self.movey += 3.2

        if self.is_jumping and self.is_falling is False:
            self.is_falling = True
            self.movey -= 33  # how high to jump

        self.rect.x += self.movex
        self.rect.y += self.movey


class Enemy(pygame.sprite.Sprite):
    """
    Spawn an enemy
    """

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'basic_enemies' + '.png'))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

    def move(self):
        """
        enemy movement
        """
        distance = 80
        speed = 8

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance * 2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1
class Level:
    def ground(lvl, gloc, tx, ty):
        ground_list = pygame.sprite.Group()
        i = 0
        if lvl == 1:
            while i < len(gloc):
                ground = Platform(gloc[i], worldy - ty, tx, ty, 'tile-ground.png')
                ground_list.add(ground)
                i = i + 1

        if lvl == 2:
            print("Level " + str(lvl))

        return ground_list

    def bad(lvl, eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1], 'enemy.png')
            enemy_list = pygame.sprite.Group()
            enemy_list.add(enemy)
        if lvl == 2:
            print("Level " + str(lvl))

        return enemy_list

    # x location, y location, img width, img height, img file
    def platform(lvl, tx, ty):
        plat_list = pygame.sprite.Group()
        ploc = []
        i = 0
        if lvl == 1:
            ploc.append((200, worldy - ty - 128, 3))
            ploc.append((300, worldy - ty - 256, 3))
            ploc.append((550, worldy - ty - 128, 4))
            while i < len(ploc):
                j = 0
                while j <= ploc[i][2]:
                    plat = Platform((ploc[i][0] + (j * tx)), ploc[i][1], tx, ty, 'tile.png')
                    plat_list.add(plat)
                    j = j + 1
                print('run' + str(i) + str(ploc[i]))
                i = i + 1

        if lvl == 2:
            print("Level " + str(lvl))

        return plat_list

class Skeleton(Character):

    def __init__(self, screen, settings):
        super().__init__(screen, settings.skeleton_sprite)

        # Need to update frame count and current frame when switching states
        self.rect = self.idle_r_frames[0].get_rect()
        self.rect.centerx = self.info['start_pos'][0]
        self.rect.bottom = self.info['start_pos'][1]

        self.frame_count = self.info['idle_frames']
        self.curr_image = self.idle_r_frames[self.curr_frame]
        self.state = State.IDLE

        self.weapon = HauntedAxe(screen, settings)

    def update(self):
        self.weapon.update(self.rect)
        self.inc_frame()
        # Update per state
        self.curr_image = self.idle_r_frames[self.curr_frame]

    def blitme(self):
        super().blitme()
        self.weapon.blitme()


class Weapon(Object):

    def __init__(self, screen, weapon_info):
        super().__init__(screen, weapon_info)

        self.active = False

        self.frames = []
        self.frame_count = weapon_info['frames']
        x_pos = self.info['x_starts']
        y_pos = self.info['y_starts']
        for frame in range(self.info['frames']):
            self.frames.append(self.image_at((x_pos[frame], y_pos[frame],
                                              self.info['size'][0], self.info['size'][1])))
        self.curr_image = self.frames[self.curr_frame]

    def activate(self, flag=False):
        self.active = flag
        self.curr_frame = 0

    def update(self, rect):
        self.rect = rect
        if self.active:
            self.inc_frame()
            self.curr_image = self.frames[self.curr_frame]

eloc = []
eloc = [300, 0]
enemy_list = Level.bad(1, eloc)

gloc = []
tx = 64
ty = 64
i = 0
while i <= (worldx / tx) + tx:
    gloc.append(i * tx)
    i = i + 1

ground_list = Level.ground(1, gloc, tx, ty)
plat_list = Level.platform(1, tx, ty)



class HauntedAxe(Weapon):
    def __init__(self, screen, settings):
        super().__init__(screen, settings.haunted_axe)

class Knife(Sprite):
    # class to manage player's throwing knives
    def __init__(self, settings, screen, character):
        # create a knife at player's position
        super(Knife, self).__init__()
        self.screen = screen

        # create knife at 0,0 and then move to correct position
        self.rect = pygame.Rect(0, 0, settings.knife_width, settings.knife_height)
        self.rect.centerx = character.rect.centerx
        self.rect.top = character.rect.top + 20

        # store position as decimal value
        self.x = float(self.rect.x)

        self.color = settings.knife_color
        self.speed = settings.knife_speed
    def update(self):
        # Move knife horizontally
        # update decimal position
        self.x += self.speed
        # update rect
        self.rect.x = self.x

    def draw_knife(self):
        # draw knife on screen
        pygame.draw.rect(self.screen, self.color, self.rect)
