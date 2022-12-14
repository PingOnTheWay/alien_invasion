import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_game) -> None:
        '''init ships and corresponding location'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        '''load the image of ships'''
        self.image = pygame.image.load('images/ship.bmp').convert()
        # make image background transparent
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()

        '''place every new ship at the bottom center of the screen'''
        self.rect.midbottom = self.screen_rect.midbottom

        # set the image location as attribute x
        self.x = float(self.rect.x)

        # moving flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        '''moving according to the moving flag'''
        # update self.x rather than rect.x and set the border
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # update the location of rectangule accroding to self.x
        self.rect.x = self.x

    def blitme(self):
        '''draw ships at the specific location'''
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = self.rect.x