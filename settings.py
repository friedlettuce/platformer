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
            'size': (48, 48),
            'start_pos': (self.screen_width / 2, self.screen_height - 50),
            'idle_frames': 4,
            'idle_y_starts': (0, 146, 146, 146),
            'idle_x_starts': (0, 49, 98, 147),
            'walk_frames': 6,
            'walk_x_starts': (49, 98, 147, 196, 245, 294),
            'walk_y_starts': (49, 49, 49, 49, 49, 49),
            'attack_frames': 10,
            'attack_y_starts': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            'attack_x_starts': (49, 98, 147, 196, 245, 294, 343, 392, 441, 490)
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
            'frames': 4,
            'y_starts': (63, 64, 65, 64),
            'x_starts': (15, 64, 113, 162)
        }
