import sys
import random

import pygame

from bullet import Bullet
from ufo import Ufo
from star import Star

def check_events(game_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_d or event.key == pygame.K_e: # e is  used
                                                        #for dvorak keyboard
                ship.go_right()

            if event.key == (pygame.K_a):
                ship.go_left()
                
            if event.key == pygame.K_SPACE:
                fire_bullet(game_settings, screen, ship, bullets)
                

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_e:
                ship.stop_right()

            if event.key == (pygame.K_a):
                ship.stop_left()
def star_creation(game_settings, screen, stars):
    if time_to_create_star(game_settings):
        new_star = Star(game_settings, screen)
        stars.add(new_star)

def time_to_create_star(game_settings):
    return random.random() < game_settings.get_star_prob()

def create_fleet(game_settings, screen, ship, ufos):
    num_ufo_x, num_ufo_rows = get_num_ufo_x_rows(game_settings, screen, ship) 

    for ufo_number in range(num_ufo_x):
        for ufo_row in range(num_ufo_rows):
            create_ufo(game_settings, screen, ufos, ufo_number, ufo_row)

def check_fleet_edges(game_settings, ufos):
    for ufo in ufos.sprites():
        if ufo.is_wall():
            change_fleet_direction_and_drop(game_settings, ufos)
            break

def change_fleet_direction_and_drop(game_settings, ufos):
    drop_fleet(ufos)
    
    game_settings.change_fleet_direction()

def drop_fleet(ufos):
    for ufo in ufos.sprites():
        ufo.drop()

def check_and_repopulate_fleet(game_settings,screen,ship, ufos, bullets):
    if len(ufos) == 0:
        create_fleet(game_settings, screen, ship, ufos)
        bullets.empty()
        

def get_num_ufo_x_rows(game_settings, screen, ship):
    return (get_num_ufo_x(game_settings, screen),
           get_num_ufo_rows(game_settings, screen, ship))
    

def get_num_ufo_x(game_settings, screen):
    ufo = Ufo(game_settings, screen)
    ufo_width = ufo.get_ufo_size()[0]
    availible_space_x = game_settings.get_screen_size()[0] - 2 * ufo_width
    return  int(availible_space_x /(2 * ufo_width))

def get_num_ufo_rows(game_settings, screen, ship):
    ufo = Ufo(game_settings, screen)
    ufo_height = ufo.get_ufo_size()[1]
    available_space_y = (game_settings.get_screen_size()[1] - (3 * ufo_height) - ship.get_size()[1])
    return int(available_space_y / (2 * ufo_height))
    

def create_ufo(game_settings, screen, ufos, ufo_number, ufo_row):
    ufo = Ufo(game_settings, screen)
    ufo.set_position(ufo_number, ufo_row)
    ufos.add(ufo)
    
            

def fire_bullet(game_settings, screen, ship, bullets):
    if len(bullets) < game_settings.get_max_num_bullets():
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(game_settings, screen, ship,ufos, bullets, stars):
    screen.fill(game_settings.background)

    for star in stars.sprites():
        star.draw()

    ship.blitme()

    ufos.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw()

    pygame.display.flip()

def update_ufos(game_settings, ufos):
    
    check_fleet_edges(game_settings, ufos)
    ufos.update()

    

def update_bullets(bullets, ufos):
    
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
            
def update_collisions(game_settings, screen, ship, ufos, bullets):

    collisions = pygame.sprite.groupcollide(bullets, ufos, True, True)

    check_and_repopulate_fleet(game_settings, screen, ship, ufos, bullets)
    

def update_stars(stars, game_settings):
    stars.update()
    for star in stars.copy():
        if star.rect.top > game_settings.get_screen_size()[1]:
            stars.remove(star)
