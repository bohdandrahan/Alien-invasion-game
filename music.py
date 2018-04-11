import pygame
pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12) 

def play_menu_music():
	pygame.mixer.music.load('audio/music/not_active.wav')
	pygame.mixer.music.play(-1)

def play_game_music():
	pygame.mixer.music.load('audio/music/active_2.wav')
	pygame.mixer.music.play(-1)