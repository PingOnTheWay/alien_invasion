import sys, pygame
from settings import Settings
from ship import Ship
from dog import Dog
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        pygame.display.set_icon(pygame.image.load("images/ufo.png"))
        self.ship = Ship(self)
        self.dog = Dog(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    
    def run_game(self):
        '''start the main function of the game'''
        while True:
            # check events
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            # update the screen
            self._update_screen()
    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        '''check weather aliens reach edges'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''move the whole fleet down and change the moving direction'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.alien_speed *= -1
    
    def _update_bullets(self):
        '''update bullet location'''
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.y < 0:
                self.bullets.remove(bullet)
    
    def _check_events(self):
        '''monitor mouse and keyboard events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
        
    def _check_keydown(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  # enter 'q' for quit
            sys.exit()
        elif event.key == pygame.K_SPACE:
            if len(self.bullets) < self.settings.bullet_allowed:
                self.bullets.add(Bullet(self))

    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        '''create aliens'''
        alien = Alien(self)
        number_aliens_x = self.settings.screen_width // (2 * alien.rect.width)
        number_aliens_y = (self.settings.screen_height - self.ship.rect.height - 
            3 * alien.rect.height) // (2 * alien.rect.height)
        for row in range(number_aliens_y):
            for num in range(number_aliens_x):
                self._creat_alien(num, row)
            

    def _creat_alien(self, number, row):
        alien = Alien(self)
        alien.x = alien.rect.width + 2 * alien.rect.width * number
        alien.y = alien.rect.height + 2 * alien.rect.height * row
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _update_screen(self):
        '''redraw the screen each loop
        Make the most recently drawn screen visible'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.dog.blitme()
        # self.alien.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
        
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
