import pygame
from pygame.sprite import Sprite

import random

class Explosion(Sprite):
    def __init__(self, game_settings, screen, ufo_exploaded):
        super().__init__()
        self.game_settings = game_settings
        self.screen = screen
        self.ufo_exploaded = ufo_exploaded[0]
        self.color = (255, random.randint(0, 255), random.randint(0, 255))

        self.rect = pygame.Rect(0, 0, self.ufo_exploaded.get_ufo_size()[0],
                               self.ufo_exploaded.get_ufo_size()[1])
        self.rect.top = self.ufo_exploaded.rect.top
        self.rect.left = self.ufo_exploaded.rect.left
        
    def remove_expired(self, explosions):
        if self.rect.width <= 2 or self.rect.height <= 2:
            explosions.remove(self)

    def change_color(self):
        for each in self.color:
            if each > 10:
                each -= 10


    def update(self):
        self.rect = self.rect.inflate(self.game_settings.get_explosion_speed())
        self.change_color()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    
