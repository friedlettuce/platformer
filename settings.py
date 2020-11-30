class Settings:

    white = [255, 255, 255]

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
            'attack_x_starts': (49, 98, 147, 196, 245, 294, 343, 392, 441, 490),
            'jump_frames': 4,
            'jump_x_starts': (49, 98, 147, 196),
            'jump_y_starts': (98, 98, 98, 98)
        }

        # Throwing Knife Settings
        self.knife_speed = 25
        self.knife_width = 6
        self.knife_height = 2
        self.knife_color = 255, 255, 255
        self.knives_allowed = 3

        self.skeleton_sprite = {
            'location': "images/basic_enemies.png",
            'size': (48, 48),
            'start_pos': (self.screen_width / 3, self.screen_height - 50),
            'idle_frames': 3,
            'idle_y_starts': (0, 0, 0),
            'idle_x_starts': (0, 49, 98)
        }

        self.haunted_axe = {
            'location': "images/basic_enemies.png",
            'size': (48, 48),
            'frames': 4,
            'y_starts': (49, 49, 49, 49),
            'x_starts': (0, 49, 98, 147)
        }
