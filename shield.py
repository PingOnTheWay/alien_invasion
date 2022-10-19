import pygame

class Shield:

    def __init__(self, game) -> None:
        self.screen = game.screen
        self.settings = game.settings

        self.rect = pygame.Rect(0,0, self.settings.shield_width, 
            self.settings.shield_height)
        
        self.rect.midbottom = game.ship.rect.midtop 
        self.rect.y -= 30

    def update_shield(self, game):
        self.rect.midbottom = game.ship.rect.midtop 
        self.rect.y -= 30

    def draw_shield(self):
        pygame.draw.rect(self.screen, self.settings.shield_color, self.rect)