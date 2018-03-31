import pygame

class Ship():

    def __init__ (self, game_settings, screen):
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)

    def get_size(self):
        return (self.rect.width, self.rect.height)
    def set_to_center(self):
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)

    def get_rect(self):
        return self.rect

    def go_right(self):
        self.moving_right = True
    
    def go_left(self):
        self.moving_left = True

    def stop_right(self):
        self.moving_right = False

    def stop_left(self):
        self.moving_left = False

    def is_wall_right(self):
        if self.rect.centerx >= self.screen_rect.width:
            return True
        else: return False

    def is_wall_left(self):
        if self.rect.centerx <= 0:
            return True
        else: return False


    def update(self):
        if self.moving_right and not self.is_wall_right():
            self.center += self.game_settings.get_ship_speed()
        if self.moving_left and not self.is_wall_left():
            self.center -= self.game_settings.get_ship_speed()

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    
