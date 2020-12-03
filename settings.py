class Settings:

    white = [255, 255, 255]

    def __init__(self):

        self.screen_width = 1000
        self.screen_height = 600
        self.screen_color = (65, 65, 65)
        self.title = "Tower Master"
        self.fps = 15
        self.background_img = "images/background_full.png"
        self.brick_ground_img = "images/brick_platform.png"

        self.player_health = 50
        self.player_w_speed = 7  # Must be a digit
        self.player_k_speed = 10
        self.player_k_time = 8
        self.player_sprite = {
            'location': "images/MainCharacter.png",
            'size': (48, 48),
            'start_pos': (self.screen_width / 2, self.screen_height - 50),
            'idle_frames': 13,
            'idle_ry_starts': (0, 147, 147, 147, 147, 147, 147, 147, 147, 147, 147, 147, 0),
            'idle_rx_starts': (0, 49, 49, 98, 98, 147, 147, 147, 98, 98, 49, 49, 0),
            'idle_ly_starts': (1032, 885, 885, 885, 885, 885, 885, 885, 885, 885, 885, 885, 1032),
            'idle_lx_starts': (0, 49, 49, 98, 98, 147, 147, 147, 98, 98, 49, 49, 0),
            'walk_frames': 6,
            'walk_rx_starts': (49, 98, 147, 196, 245, 294),
            'walk_ry_starts': (49, 49, 49, 49, 49, 49),
            'walk_lx_starts': (49, 98, 147, 196, 245, 294),
            'walk_ly_starts': (983, 983, 983, 983, 983, 983),
            'attack_frames': 10,
            'attack_ry_starts': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            'attack_rx_starts': (49, 98, 147, 196, 245, 294, 343, 392, 441, 490),
            'attack_ly_starts': (1032, 1032, 1032, 1032, 1032, 1032, 1032, 1032, 1032, 1032),
            'attack_lx_starts': (49, 98, 147, 196, 245, 294, 343, 392, 441, 490),
            'jump_frames': 4,
            'jump_rx_starts': (49, 98, 147, 196),
            'jump_ry_starts': (98, 98, 98, 98),
            'jump_lx_starts': (49, 98, 147, 196),
            'jump_ly_starts': (934, 934, 934, 934),
            'dash_frames': 6,
            'dash_rx_starts': (58, 107, 156, 205, 254, 303),
            'dash_ry_starts': (201, 203, 203, 202, 202, 202),
            'dash_lx_starts': (64, 112, 161, 211, 260, 309),
            'dash_ly_starts': (841, 843, 843, 842, 842, 842)
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
            'start_pos': (self.screen_width / 3, self.screen_height - 56),
            'idle_frames': 3,
            'idle_ry_starts': (0, 0, 0),
            'idle_rx_starts': (0, 49, 98)
        }

        self.haunted_axe = {
            'location': "images/basic_enemies.png",
            'size': (48, 48),
            'frames': 4,
            'y_starts': (49, 49, 49, 49),
            'x_starts': (0, 49, 98, 147)
        }

        self.platform = {
            'location': "images/basic_enemies.png",
            'size': (48, 48),
            'start_pos': (self.screen_width / 3, self.screen_height - 56),
            'idle_frames': 3,
            'idle_ry_starts': (0, 0, 0),
            'idle_rx_starts': (0, 49, 98)
        }
