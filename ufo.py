import pygame 
from pygame.sprite import Sprite

class Ufo(Sprite):
    def __init__(self, game_settings, screen):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load('images/ufo.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def set_position(self, ufo_number, ufo_row):
        self.set_position_x(ufo_number)
        self.set_position_y(ufo_row)

    def set_position_x(self, ufo_number):
        self.x = self.get_ufo_size()[0] * (1 + 2 * ufo_number)
        self.rect.x = self.x

    def set_position_y(self, ufo_row):
        self.y = self.get_ufo_size()[1] * (1 + 2 * ufo_row)
        self.rect.y = self.y

    def get_ufo_size(self):
        return (self.rect.width, self.rect.height)
        

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.move_side()

    def move_side(self):
        self.x += (self.game_settings.get_ufo_speed() * self.game_settings.get_fleet_direction())
        self.rect.x =  self.x

    def drop(self):
        self.y += self.game_settings.get_ufo_speed_drop()
        self.rect.y = self.y

    def is_wall(self):
        return self.is_wall_left() or self.is_wall_right()

    def is_wall_left(self):
        if self.rect.left <= 0:
            return True
        else: return False

    def is_wall_right(self):
        if self.rect.right >= self.game_settings.get_screen_size()[0]:
            return True
        else: return False
        
