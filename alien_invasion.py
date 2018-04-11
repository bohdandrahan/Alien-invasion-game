import sys
import pygame
from pygame.sprite import Group


from settings import Settings
from game_stats import GameStats
from ship import Ship
from ufo import Ufo
import game_functions

from button import Button
from scoreboard import CurrentScore
from scoreboard import HiScore
from scoreboard import Level
from life import Life
import music

def run_game():

    pygame.init()

    music.play_menu_music()

    game_settings = Settings()

    screen = pygame.display.set_mode(game_settings.get_screen_size())

    pygame.display.set_caption('Alien Invasion')

    stats = GameStats(game_settings)

    ship = Ship(game_settings, screen)
    
    ufos = Group()

    bullets = Group()

    stars = Group()

    explosions = Group()

    play_button = Button(game_settings, screen, 'Play')

    current_score = CurrentScore(game_settings, screen, stats)

    hi_score = HiScore(game_settings, screen, stats)

    level = Level(game_settings, screen, stats)

    lifes = Group()

    while True:

        game_functions.check_events(game_settings, screen, 
                                   stats, ship, ufos, bullets, play_button, lifes)

        game_functions.star_creation(game_settings, screen, stars)

        if stats.game_active:

            ship.update()
            game_functions.update_bullets(bullets,ufos)
            game_functions.update_ufos(game_settings, screen, stats,
                                      ship, ufos, bullets, explosions, lifes) 
   

        game_functions.update_screen(game_settings, screen, stats, ship, ufos, bullets, stars,
                                    explosions, play_button, current_score, hi_score, level, lifes)

 
        game_functions.update_collisions(game_settings, screen,
                                        stats, ship, ufos, bullets, explosions, current_score)
        game_functions.update_explosions(game_settings, explosions)
        
        game_functions.update_stars(stars, game_settings)

run_game()
