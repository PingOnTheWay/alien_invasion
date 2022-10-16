class Settings:
    '''save all the settings of Alien Invasion'''

    def __init__(self) -> None:
        '''init game settings'''
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135,206,250)

        # ship
        self.ship_speed = 2.4
        self.ship_limit = 3

        # bullets
        self.bullet_speed = 3.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 5

        # alien
        self.alien_speed = 1.0
        self.fleet_drop_speed = 8
        # -1: move left; 1: move right
        self.fleet_direction = -1

        # game tempo
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        '''init speed settingss'''
        self.ship_speed = 3.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = -1
    
    def speedup(self):
        '''accelerate'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

