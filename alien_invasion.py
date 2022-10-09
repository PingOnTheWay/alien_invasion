import sys, pygame
from settings import Settings
from ship import Ship
from dog import Dog

class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.icon = pygame.image.load("images/ufo.png")
        pygame.display.set_icon(self.icon)
        self.ship = Ship(self)
        self.dog = Dog(self)

    
    def run_game(self):
        '''start the main function of the game'''
        while True:
            # check events
            self._check_events()
            # update the screen
            self._update_screen()
    
    def _check_events(self):
        '''monitor mouse and keyboard events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        '''redraw the screen each loop
        Make the most recently drawn screen visible'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.dog.blitme()
        pygame.display.flip()
        
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
