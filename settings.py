class Settings:

    def __init__(self):

        self.screen_width = 1000
        self.screen_height = 600
        self.screen_color = (65, 65, 65)
        self.title = "Tower Master"
        self.fps = 20

        self.player_w_speed = 7  # Must be a digit
        self.player_sprite = {
            'location': "images/MainCharacter_transparent.png",
            'size': (22, 43),
            'start_pos': (self.screen_width / 2, self.screen_height - 50),
            'idle_frames': 4,
            'idle_y_starts': (3, 3, 3, 3),
            'idle_x_starts': (12, 61, 113, 162)
        }
