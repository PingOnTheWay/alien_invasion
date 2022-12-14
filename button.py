import pygame.font
import pygame

class Button:

    def __init__(self, game, msg, *args) -> None:
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if not args:
            self.rect.topleft = self.screen_rect.topleft
        else:
            self.rect.right = self.screen_rect.right - (args[0] - 1) * self.width
            self.rect.top = self.screen_rect.top

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, 
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        # pygame.draw.rect(self.screen , self.button_color, self.rect) 不好，创建了一个新的rect
        self.screen.blit(self.msg_image, self.msg_image_rect)