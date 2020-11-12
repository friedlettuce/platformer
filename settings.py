class Settings:

    def __init__(self):

        self.screen_width = 1000
        self.screen_height = 600
        self.screen_color = (65, 65, 65)
        self.title = "Tower Master"
        self.fps = 15
        self.background_img = "images/background_full.png"

        self.player_w_speed = 7  # Must be a digit
        self.player_sprite = {
            'location': "images/MainCharacter.png",
            'size': (22, 43),
            'start_pos': (self.screen_width / 2, self.screen_height - 50),
            'idle_frames': 4,
            'idle_y_starts': (3, 53, 103, 152),
            'idle_x_starts': (12, 12, 13, 13),
            'walk_frames': 3,
            'walk_x_starts': (12, 61, 110),
            'walk_y_starts': (53, 53, 53),
            'attack_frames': 13,
            'attack_y_starts': (3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
            'attack_x_starts': (12, 61, 113, 162, 211, 260, 309, 358, 407, 452, 501, 550, 599)
        }

        self.skeleton_sprite = {
            'location': "images/basic_enemies.png",
            'size': (22, 43),
            'start_pos': (self.screen_width / 3, self.screen_height - 50),
            'idle_frames': 2,
            'idle_y_starts': (3, 3),
            'idle_x_starts': (12, 55)
        }

        self.haunted_axe = {
            'location': "images/basic_enemies.png",
            'size': (10, 10),
            'frames': 2,
            'y_starts': (),
            'x_starts': ()
        }
