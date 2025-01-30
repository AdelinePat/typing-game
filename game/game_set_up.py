import pygame
import string
from game.__settings__ import FPS
from game.game_functions import clock_tick
from game.manage_input import input_expression

def game_set_up(screen,clock,game_mode,player):
    if player != '':
        user_input = player
    else: 
        user_input = ''
    current_background = screen.background()
    while True:
        screen.screen.blit(current_background, (0, 0))
        user_print = pygame.font.Font('assets/fonts/Coolvetica Rg.otf').render(user_input, True, 'black', 'white')
        user_print_rect = user_print.get_rect(center= (screen.width//2, screen.height//2))
        screen.screen.blit(user_print, user_print_rect)
        game_mode, user_input, correct_input = input_expression(game_mode, user_input, 9)
        match correct_input:
            case True:
                player = user_input
                return "in_game", game_mode, player
            case False:
                return "main_menu", game_mode, player
            case 'quit':
                return "off", None, None
        clock_tick(clock,FPS)
