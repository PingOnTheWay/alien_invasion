class GameStats:
    '''track game statistics'''

    def __init__(self, game) -> None:
        '''init statistics'''
        self.settings = game.settings
        self.game_active = False
        self.high_score = self._load_high_score()
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        try:
            file = open("data.txt","r")
        except:
            return 0
        else:
            score = int(file.read())
            file.close()
            return score

