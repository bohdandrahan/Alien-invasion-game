import pygame.font
import pygame

from pygame.sprite import Group
    
    
class Scoreboard():
    def __init__(self, game_settings, screen, stats):
        self.game_settings = game_settings
        self.screen = screen
        self.stats = stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('font/Boxy-Bold.ttf', 45)

        self.get_rect()

    def get_image(self):
        return self.font.render(self.get_text(),
            True, self.text_color, self.game_settings.get_background())

    def get_rect(self):
        self.rect = self.get_image().get_rect()
        self.set_location()
        return self.rect

    def set_location(self):
        #abstract method
        pass

    def get_text(self):
        #abstract method
        pass

    def show(self):
        self.screen.blit(self.get_image(), self.get_rect())

class CurrentScore(Scoreboard):

    def get_text(self):
        return str(self.stats.get_score())

    def set_location(self): 
        self.rect.right = self.game_settings.get_screen_size()[0] - 20
        self.rect.top = 20

class HiScore(Scoreboard):

    def get_text(self):
        return str(self.stats.get_hi_score())

    def set_location(self):
        self.rect.centerx = self.game_settings.get_screen_size()[0] / float(2)
        self.rect.top = 20

class Level(Scoreboard):
    def get_text(self):
        return str(self.stats.get_lvl())

    def set_location(self):
        self.rect.right = self.game_settings.get_screen_size()[0] - 20
        self.rect.top = 85







