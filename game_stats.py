class GameStats:
    '''track game statistics'''

    def __init__(self, game) -> None:
        '''init statistics'''
        self.settings = game.settings
        self.game_active = False
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
