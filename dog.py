import pygame

class Dog:

    def __init__(self, ai_game) -> None:
        '''init dogs and corresponding location'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        '''load the image of ships'''
        self.image = pygame.transform.scale(pygame.image.load('images/dog.png'),
                 (55,55))
        self.rect = self.image.get_rect()

        '''place every new ship at the bottom center of the screen'''
        self.rect.center = self.screen_rect.center

    def blitme(self):
        '''draw ships at the specific location'''
        self.screen.blit(self.image,self.rect)

