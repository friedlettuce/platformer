import pygame


class Object:

    def __init__(self, screen, img, frames, size, init_pos):
        self.screen = screen

        self.frames = []
        self.curr_frame = 0
        for frame in range(frames):
            self.frames.append(pygame.transform.smoothscale(
                pygame.image.load(img + str(frame) + ".png"), size))

        self.rect = self.frames[0].get_rect()
        self.rect.centerx = init_pos[0]
        self.rect.bottom = init_pos[1]

        self.moving_right = False
        self.moving_left = False

    def inc_frame(self):
        self.curr_frame = (self.curr_frame + 1) % len(self.frames)

    def blitme(self):
        self.screen.blit(self.frames[self.curr_frame], self.rect)


class Player(Object):

    def __init__(self, screen, settings):
        super().__init__(screen, "stickman", settings.player_frames, settings.player_size, (
            settings.screen_width / 2, settings.screen_height - settings.player_size[1]
        ))
        self.walking_speed = settings.player_w_speed

    def move_left(self, flag=True):
        self.moving_left = flag

    def move_right(self, flag=True):
        self.moving_right = flag

    def update(self):
        if self.moving_right:
            self.rect.centerx += self.walking_speed
        elif self.moving_left:
            self.rect.centerx -= self.walking_speed

        self.inc_frame()
