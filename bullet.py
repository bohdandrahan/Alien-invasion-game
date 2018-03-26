import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game_settings, screen, ship):
        super().__init__()

        self.game_settings = game_settings
        self.screen = screen
        self.ship = ship

        self.rect = pygame.Rect(0, 0,
                               self.game_settings.get_bullet_size()[0],
                               self.game_settings.get_bullet_size()[1])
        self.rect.centerx = ship.get_rect().centerx
        self.rect.top = ship.get_rect().top
        
        self.y = float(self.rect.y)

        self.color = game_settings.get_bullet_color()

    def update(self):
            self.y -= self.game_settings.get_bullet_speed()
            self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        



