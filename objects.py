import pygame
from enum import Enum


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
        image = pygame.Surface(rect.size)
        image.blit(self.sprite_sheet, (0, 0), rect)
        return image

    def blitme(self):
        self.screen.blit(self.curr_image, self.rect)


class State(Enum):
    IDLE = 0
    WALK = 1
    ATTACK = 2


class Character(Object):

    def __init__(self, screen, sprite_info):
        super().__init__(screen, sprite_info)

        self.state = None
        self.moving_right = False
        self.moving_left = False

        self.idle_frames = []
        self.walk_frames = []
        self.attack_frames = []

        x_pos = self.info['idle_x_starts']
        y_pos = self.info['idle_y_starts']
        for frame in range(self.info['idle_frames']):
            self.idle_frames.append(self.image_at((x_pos[frame], y_pos[frame],
                                                   self.info['size'][0], self.info['size'][1])))
        # Points to which array of frames to use
        self.curr_frames = None

    def move_left(self, flag=True):
        if flag and self.state is not State.WALK:
            self.walk_state()
        elif not self.moving_right and self.state is not State.IDLE:
            self.idle_state()
        self.moving_left = flag

    def move_right(self, flag=True):
        if flag and self.state is not State.WALK:
            self.walk_state()
        elif not self.moving_left and self.state is not State.IDLE:
            self.idle_state()
        self.moving_right = flag

    def idle_state(self):
        self.state = State.IDLE
        self.curr_frame = 0
        self.frame_count = self.info['idle_frames']
        self.curr_frames = self.idle_frames

    def walk_state(self):
        if self.state is State.ATTACK:
            return
        self.state = State.WALK
        self.curr_frame = 0
        self.frame_count = self.info['walk_frames']
        self.curr_frames = self.walk_frames

    def attack_state(self):
        if self.state == State.ATTACK:
            return
        self.state = State.ATTACK
        self.curr_frame = 0
        self.frame_count = self.info['attack_frames']
        self.curr_frames = self.attack_frames


class Player(Character):

    def __init__(self, screen, settings):
        super().__init__(screen, settings.player_sprite)

        self.walking_speed = settings.player_w_speed

        self.rect = self.idle_frames[0].get_rect()
        self.rect.centerx = self.info['start_pos'][0]
        self.rect.bottom = self.info['start_pos'][1]

        x_pos = self.info['walk_x_starts']
        y_pos = self.info['walk_y_starts']
        for frame in range(self.info['walk_frames']):
            self.walk_frames.append(self.image_at((x_pos[frame], y_pos[frame],
                                                   self.info['size'][0], self.info['size'][1])))
        x_pos = self.info['attack_x_starts']
        y_pos = self.info['attack_y_starts']
        for frame in range(self.info['attack_frames']):
            self.attack_frames.append(self.image_at((x_pos[frame], y_pos[frame],
                                                     self.info['size'][0], self.info['size'][1])))
        self.idle_state()

    def update(self):

        if self.moving_right:
            self.rect.centerx += self.walking_speed
        elif self.moving_left:
            self.rect.centerx -= self.walking_speed

        if self.state is State.ATTACK and self.curr_frame+1 is self.info['attack_frames']:
            self.idle_state()
        else:
            self.inc_frame()

        self.curr_image = self.curr_frames[self.curr_frame]


class Skeleton(Character):

    def __init__(self, screen, settings):
        super().__init__(screen, settings.skeleton_sprite)

        # Need to update frame count and current frame when switching states
        self.rect = self.idle_frames[0].get_rect()
        self.rect.centerx = self.info['start_pos'][0]
        self.rect.bottom = self.info['start_pos'][1]

        self.frame_count = self.info['idle_frames']
        self.curr_image = self.idle_frames[self.curr_frame]
        self.state = State.IDLE

        self.weapon = HauntedAxe(screen, settings)

    def update(self):
        self.weapon.update(self.rect)
        self.inc_frame()
        # Update per state
        self.curr_image = self.idle_frames[self.curr_frame]

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


class HauntedAxe(Weapon):
    def __init__(self, screen, settings):
        super().__init__(screen, settings.haunted_axe)
