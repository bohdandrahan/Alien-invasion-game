import pygame
from pygame.sprite import Sprite
import time
import random

class Star(Sprite):
    def __init__ (self, game_settings, screen):
        super().__init__()

        self.game_settings = game_settings
        self.screen = screen

        self.rect = pygame.Rect(0, 0, random.randint(1, 10), random.randint(1, 10))
        self.x = random.randint(0, game_settings.get_screen_size()[0])
        self.rect.centerx = self.x
        self.rect.bottom = 0
        self.color = (random.randint(0, 255), random.randint(0, 255), 255)
        self.y = self.rect.y

    def update(self):
        self.y += self.game_settings.get_star_speed()
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


        
