# from display.display_game_elements import display_hearts, display_score_in_game
from display.display_menu import get_buttons, display_mode_menu
from display.display_scores import display_scores, display_empty_score
import pygame

from menu.in_score_menu import in_score_menu
from menu.in_main_menu import in_main_menu
from menu.in_mode_menu import in_mode_menu
from menu.in_start_menu import in_start_menu
# from display.display_models import Button
# from display.display_models import Screen
# from game.scores.Scores import Scores
from game.game_functions import init_game_functions, game_off, clock_tick
from game.game_round import run_new_game
from game.game_set_up import run_set_up_game
from __settings__ import TEXT_COLOR,TEXT_COLOR_DARK
from display.display_models.__settings__ import BACKGROUND_IMAGE, BACKGROUND_IMAGE_MENU
from display.display_menu import game_over_screen
from __settings__ import SCREEN, FPS


def menu_display():
    clock, player, game_mode, game_menu, language_mode = init_game_functions()
    current_background = SCREEN.background(BACKGROUND_IMAGE, "Fruit Slicer")   
    main_menu_button, main_button_list = get_buttons()
    run = True
    SCREEN.screen.blit(current_background, (0,0))
    while run:
        clock_tick(clock, FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    game_menu = "main_menu"

            match game_menu:
                case "start_menu":
                    game_menu = in_start_menu(clock, FPS, main_menu_button)

                case "main_menu":
                    game_menu = in_main_menu(clock, FPS, main_button_list)

                case "score_menu":
                    game_menu = in_score_menu(clock, FPS)
                   
                case "mode_menu":
                    game_menu, language_mode, game_mode = in_mode_menu(clock, FPS, game_mode, language_mode)     

                case "game_on":
                    game_menu, player = run_set_up_game(SCREEN, clock, FPS, player)

                case "in_game":
                    game_menu, player_score = run_new_game(SCREEN, clock, FPS, game_mode, player)

                case "menu_game_over":
                    game_menu = game_over_screen(player_score)

                case "exit_menu":
                    exit()

        pygame.display.update() 
menu_display()