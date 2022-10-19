import pygame.font

class Scoreboard:

    def __init__(self, game) -> None:
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.game_stats = game.game_stats

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,40)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        rounded_score = round(self.game_stats.score, -1)
        score_str = f"score : {rounded_score}"
        self.score_image = self.font.render(score_str, True, self.text_color, 
                self.settings.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = 300
        self.score_rect.top = self.screen_rect.top

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)

    def prep_high_score(self):
        self.high_score_image = self.font.render(str(self.game_stats.high_score),
                True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = 300
        self.high_score_rect.top = self.score_rect.height

    def prep_level(self):
        self.level_image = self.font.render(str(self.game_stats.level),True,
                self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 10
        self.level_rect.top = 50

    def check_hight_score(self):
        if self.game_stats.score > self.game_stats.high_score:
            self.game_stats.high_score = self.game_stats.score
            self.prep_high_score()