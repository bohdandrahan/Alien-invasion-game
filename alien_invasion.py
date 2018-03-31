import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
from ufo import Ufo
import game_functions


def run_game():
    pygame.init()

    game_settings = Settings()

    screen = pygame.display.set_mode(game_settings.get_screen_size())

    pygame.display.set_caption('Alien Invasion')
    stats = GameStats(game_settings)
    
    ship = Ship(game_settings, screen)
    
    ufos = Group()

    bullets = Group()

    stars = Group()

    explosions = Group()


    game_functions.create_fleet(game_settings, screen, ship, ufos)

    while True:

        game_functions.check_events(game_settings, screen, ship, bullets)

        game_functions.star_creation(game_settings, screen, stars)

        if stats.game_active:

            ship.update()
            game_functions.update_bullets(bullets,ufos)
            game_functions.update_ufos(game_settings, screen, stats, ship, ufos, bullets, explosions)
    
        game_functions.update_screen(game_settings, screen, ship, ufos, bullets, stars, explosions)
        
            
        
        game_functions.update_collisions(game_settings, screen, ship, ufos, bullets, explosions)

        game_functions.update_explosions(game_settings, explosions)
        
        game_functions.update_stars(stars, game_settings)

run_game()
