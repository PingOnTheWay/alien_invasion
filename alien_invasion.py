import math
import sys, pygame

from time import sleep
from settings import Settings
from ship import Ship
from dog import Dog
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        pygame.display.set_icon(pygame.image.load("images/ufo.png"))

        # create an object to save game statistics
        self.game_stats = GameStats(self)
        self.scoreboard = Scoreboard(self)

        self.ship = Ship(self)
        self.dog = Dog(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.buttons = list()
        self._create_buttons()

    def _create_buttons(self):
        for i in range(4):
            if i == 0:
                self.buttons.append(Button(self, "Play"))
            else:
                button = Button(self, f"level {i}", i)
                self.buttons.append(button)
    
    def run_game(self):
        '''start the main function of the game'''
        while True:
            # check events
            self._check_events()
            if self.game_stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                # update the screen
            self._update_screen()

    def _ship_hit(self):
        '''response to spaceship being hit by aliens'''

        # ship - 1
        self.game_stats.ships_left -= 1
        self.scoreboard.prep_ships()
        if self.game_stats.ships_left < 1:
            self.game_stats.game_active = False
            pygame.mouse.set_visible(True)
        else:
            # clear all rest aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet of aliens and place ship back to the postions
            self._create_fleet()
            self.ship.center_ship()

            # pause
            sleep(1)

    def _save_high_score(self):
        file = open("data.txt", "w", encoding="UTF-8")
        file.write(str(self.game_stats.high_score))
        file.close()
    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        # check whether there are collisions between aliens and ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()


    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        '''check whether aliens reach edges'''
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
        # check if aliens are shoot
        self.__check_bullets_aliens_collisions()

    def __check_bullets_aliens_collisions(self):
        # remove bullets and aliens with collison
        collisions = pygame.sprite.groupcollide(self.aliens, self.bullets, True,
            False)
        if collisions:
            self.game_stats.score += self.settings.alien_points * len(collisions)
            self.scoreboard.prep_score()
            self.scoreboard.check_hight_score()

        # if all aliens were killed, generate a new fleet
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.speedup()

            self.game_stats.level += 1
            self.scoreboard.prep_level()
    
    def _check_events(self):
        '''monitor mouse and keyboard events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._save_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_level_buttons(mouse_pos)                    

    def _check_level_buttons(self, mouse_pos):
        for i in range(1,4):
            if self.buttons[i].rect.collidepoint(mouse_pos) and not \
                self.game_stats.game_active:
                    self.settings.level = math.sqrt(i)
    
    def _check_play_button(self, mouse_pos):
        # the new game starts only when the player clicks the button and the 
        # game is not active
        if self.buttons[0].rect.collidepoint(mouse_pos) and not \
            self.game_stats.game_active:
                self.settings.initialize_dynamic_settings()
                self._start_game()
    
    def _start_game(self):
        self.game_stats.game_active = True
        self.game_stats.reset_stats()
        self.scoreboard.prep_score()
        self.scoreboard.prep_level()
        self.scoreboard.prep_ships()

        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()

        # hide mouse
        pygame.mouse.set_visible(False)
        
    def _check_keydown(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  # enter 'q' for quit
            self._save_high_score()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            if len(self.bullets) < self.settings.bullet_allowed:
                self.bullets.add(Bullet(self))
        elif event.key == pygame.K_p:
            self.settings.initialize_dynamic_settings()
            self._start_game()
        elif event.key == pygame.K_ESCAPE:
            pygame.mouse.set_visible(True)
            self.game_stats.game_active = False
        elif event.key == pygame.K_r:
            pygame.mouse.set_visible(False)
            self.game_stats.game_active = True

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
        
        self.scoreboard.show_score()

        if not self.game_stats.game_active:
            for button in self.buttons:
                button.draw_button()
        pygame.display.flip()
        
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
