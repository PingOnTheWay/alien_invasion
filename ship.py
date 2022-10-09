import pygame

class Ship:

    def __init__(self, ai_game) -> None:
        '''init ships and corresponding location'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        '''load the image of ships'''
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        '''place every new ship at the bottom center of the screen'''
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''draw ships at the specific location'''
        self.screen.blit(self.image,self.rect)
