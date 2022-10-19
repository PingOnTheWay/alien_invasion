import pygame
from pygame.sprite import Sprite

class AlienBullet(Sprite):
    def __init__(self, game, alien) -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0,self.settings.alien_bullet_width,
            self.settings.alien_bullet_height)
        self.rect.midtop = alien.rect.midbottom
        self.y = float(self.rect.y)
    
    def update(self):
        '''move bullet downstairs'''
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
