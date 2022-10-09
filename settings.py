class Settings:
    '''save all the settings of Alien Invasion'''

    def __init__(self) -> None:
        '''init game settings'''
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135,206,250)
        self.ship_speed = 1.5