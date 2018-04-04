import sys
import random
from time import sleep

import pygame

from bullet import Bullet
from ufo import Ufo
from star import Star
from explosion import Explosion

def check_events(game_settings, screen, stats, ship, ufos, bullets,  play_button):
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

        if not stats.game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(game_settings, screen, stats, ship, ufos, bullets, play_button, mouse_x, mouse_y)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    set_up_new_game(game_settings, screen, stats, ship, ufos, bullets)
            

def check_play_button(game_settings, screen, stats, ship, ufos, bullets, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        set_up_new_game(game_settings, screen, stats, ship, ufos, bullets)
        
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

def check_and_repopulate_fleet(game_settings,screen,stats, ship, ufos, bullets):
    if len(ufos) == 0 and stats.game_active:
        level_up(game_settings, stats)
        create_fleet(game_settings, screen, ship, ufos)
        bullets.empty()

def level_up(game_settings, stats):
    print('level_up')
    game_settings.increase_speed()

def get_num_ufo_x_rows(game_settings, screen, ship):
    return (get_num_ufo_x(game_settings, screen),
           get_num_ufo_rows(game_settings, screen, ship))
    

def get_num_ufo_x(game_settings, screen):
    ufo = Ufo(game_settings, screen)
    ufo_width = ufo.get_size()[0]
    availible_space_x = game_settings.get_screen_size()[0] - 2 * ufo_width
    return  int(availible_space_x /(2 * ufo_width))

def get_num_ufo_rows(game_settings, screen, ship):
    ufo = Ufo(game_settings, screen)
    ufo_height = ufo.get_size()[1]
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


def update_screen(game_settings, screen, stats, ship, ufos, bullets, stars, explosions, play_button):
    screen.fill(game_settings.background)


    for star in stars.sprites():
        star.draw()

    ship.blitme()

    ufos.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw()

    for explosion in explosions.sprites():
        explosion.draw()

    if not stats.game_active:
        play_button.draw_button()
        
    pygame.display.flip()

def update_ufos(game_settings,screen, stats, ship, ufos, bullets, explosions):
    
    check_fleet_edges(game_settings, ufos)
    ufos.update()

    if ufo_toched_bottom_or_ship(game_settings,screen, ship, ufos, explosions):
        stats.lost_life()

        if stats.get_ships_left() != 0:
            set_up_new_life(game_settings,screen, ship, ufos, bullets)

        else:
            game_over(stats)

def set_up_new_life(game_settings, screen, ship, ufos, bullets):
    ship.set_to_center()
    ufos.empty()
    bullets.empty()
    create_fleet(game_settings, screen, ship, ufos)

    #sleep(0.5)

def set_up_new_game(game_settings, screen, stats, ship, ufos, bullets):
    game_settings.initialize_dynamic_settings()
    stats.activate_game()
    set_up_new_life(game_settings, screen, ship, ufos, bullets)
    stats.reset_stats()

def game_over(stats):
    stats.disactive_game()
    print('game_over')
    pass


def ufo_toched_bottom_or_ship(game_settings,screen, ship, ufos, explosions):

   return ufos_toched_bottom(game_settings,screen, ufos, explosions) or ufos_toched_ship(game_settings, screen, ship,  ufos, explosions)


def ufos_toched_bottom(game_settings,screen, ufos, explosions):
    
    result = False
    for ufo in ufos:
        if ufo.toched_bottom():
            add_new_explosion(game_settings, screen, explosions, ufo)
            print('hit bottom')
            result = True
    return result

def ufos_toched_ship(game_settings,screen, ship, ufos, explosions):
    if pygame.sprite.spritecollideany(ship, ufos):
        add_new_explosion(game_settings, screen, explosions, ship)

        print('ship is hit')
        return True

def update_bullets(bullets, ufos):
    
    bullets.update()

    for bullet in bullets:
        bullet.remove_missed(bullets)

            
def update_collisions(game_settings, screen, stats, ship, ufos, bullets, explosions):

    collisions = pygame.sprite.groupcollide(bullets, ufos, True, True)
    if collisions: expload(game_settings, screen, collisions, explosions)

    check_and_repopulate_fleet(game_settings, screen, stats, ship, ufos, bullets)

def expload(game_settings, screen,  collisions, explosions):
    for each in collisions:
        add_new_explosion(game_settings, screen, explosions, collisions[each][0])

def add_new_explosion(game_settings,screen, explosions, obj_exploaded):
    new_explosion = Explosion(game_settings, screen, obj_exploaded)
    explosions.add(new_explosion)


def update_explosions(game_settings, explosions):
    explosions.update()

    for explosion in explosions:
        explosion.remove_expired(explosions)

def update_stars(stars, game_settings):
    stars.update()
    for star in stars.copy():
        if star.rect.top > game_settings.get_screen_size()[1]:
            stars.remove(star)
