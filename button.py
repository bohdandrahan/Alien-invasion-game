import pygame.font
import pygame

class Button():
    def __init__(self, game_settings, screen, msg, color = (0, 0, 0, 0), 
            text_color = (255, 255, 255)):
        self.screen = screen
        self.game_settings = game_settings
        self.msg = str(msg)

        self.width, self.height = 1, 1
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.Font('font/Boxy-Bold.ttf', 150)

        self.prep_msg()

        self.rect.center = self.screen.get_rect().center

    
    def prep_msg(self):
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.color)
        self.rect = self.msg_image.get_rect()

    def draw_button(self):

        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.rect)

  

