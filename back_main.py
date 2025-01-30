import pygame
from game.scores.Player_attributes import *
from game.in_game import *
from game.main_menu import *
from game.game_set_up import *
from game.game_functions import game_init, game_off

screen,clock = game_init()
def main():
    try:
        player=''
        game_mode = 'normal'
        game_menu = 'main_menu'
        while True:
            match game_menu:
                case 'main_menu':
                    game_menu = main_menu(screen,clock)

                case 'game_set_up':
                    game_menu, game_mode, player = game_set_up(screen,clock,game_mode,player)

                case 'in_game':
                    game_menu = in_game(screen,clock,game_mode,player)

                case 'game_off'| _:
                    game_off()
    except KeyboardInterrupt:
        game_off()
    except pygame.error:
        game_off()

main()