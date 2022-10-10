import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, game) -> None:
        super().__init__()

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/alien.bmp").convert()
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()
        # self.rect.topleft = self.screen_rect.topleft
        self.rect.x = 0
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    # def blitme(self):
    #     self.screen.blit(self.image,self.rect)
