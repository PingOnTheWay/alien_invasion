import sys
import pygame

class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        '''start the main function of the game'''
        while True:
            # monitor mouse and keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Make the most recently drawn screen visible
            pygame.display.flip()
        
if __name__ == "main":
    ai = AlienInvasion()
    ai.run_game()