import pygame
import string
from game.__settings__ import FPS
from game.game_functions import clock_tick

def main_menu(screen, clock):
    current_background = screen.background()
    screen.screen.blit(current_background, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "game_off"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 'game_set_up'
        clock_tick(clock,FPS)