import pygame
from pygame.sprite import Sprite

import random

class Explosion(Sprite):
    def __init__(self, game_settings, screen, obj_exploaded):
        super().__init__()
        self.game_settings = game_settings
        self.screen = screen
        self.obj_exploaded = obj_exploaded
        self.color = (255, random.randint(0, 255), random.randint(0, 255))

        self.rect = pygame.Rect(0, 0, self.obj_exploaded.get_size()[1],
                               self.obj_exploaded.get_size()[1])
        self.rect.top = self.obj_exploaded.rect.top
        self.rect.left = self.obj_exploaded.rect.left
        
    def remove_expired(self, explosions):
        if self.rect.width <= 2 or self.rect.height <= 2:
            explosions.remove(self)

    def change_color(self):
        pass

    def update(self):
        self.rect = self.rect.inflate(self.game_settings.get_explosion_speed())
        self.change_color()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    
