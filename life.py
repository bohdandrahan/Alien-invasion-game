import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

class Life(Sprite):
    def __init__(self, game_settings, screen, number):
        super().__init__()
        
        self.number = number
        self.game_settings = game_settings
        self.screen = screen
        self.image = pygame.image.load('images/life.png')
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0 

    def set_position(self, number):
        self.left = float(20 + (20 + self.rect.width) * number)
        self.rect.left = self.left

        self.top = 20

    def get_num(self):
        return self.number

    def get_size(self):
        return (self.rect.width, self.rect.height)

    def blitme(self):
        self.screen.blit(self.image, self.rect)



