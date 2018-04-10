import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

class LifeBoard():
    def __init__(self, game_settings, screen, stats):
        self.game_settings = game_settings
        self.screen = screen
        self.stats = stats
        self.lifes = Group()

    def init_lifes(self):
        print('init_lifes')
        for each in range(self.stats.get_ship_left()):
            life = Life(self.game_settings, self.screen, self)
            self.lifes.add(life) 
        print(self.lifes)

    def get_lifes(self):
        return self.lifes

    def show(self):
        for each in self.lifes:
            each.blitme()

class Life(Sprite):
    def __init__(self, game_settings, screen, life_board):
        super().__init__()
        
        self.game_settings = game_settings
        self.screen = screen
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.left = 0 #20 + (len(life_board.get_lifes())) * (self.rect.width + 20)
        self.rect.top = 0 #20

    def blitme(self):
        self.screen.blit(self.image, self.rect)



