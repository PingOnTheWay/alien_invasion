class Settings:
    '''save all the settings of Alien Invasion'''

    def __init__(self) -> None:
        '''init game settings'''
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135,206,250)
        self.ship_speed = 1.5

        # bullets
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3