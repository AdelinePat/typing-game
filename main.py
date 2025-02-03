from __settings__ import SCREEN, FPS
import pygame
from display.display_models.__settings__ import BACKGROUND_IMAGE
from display.display_models.translation_manager import TranslationManager
from display.display_menu import get_main_menu_button, game_over_screen
from menu.in_score_menu import in_score_menu
from menu.in_main_menu import in_main_menu
from menu.in_mode_menu import in_mode_menu
from menu.in_start_menu import in_start_menu
from game.game_functions import init_game_functions, clock_tick
from game.game_round import run_new_game
from game.game_set_up import run_set_up_game


translate_all = TranslationManager()

def main():
    clock, player, game_mode, game_menu, language_mode = init_game_functions()
    current_background = SCREEN.background(BACKGROUND_IMAGE, translate_all.translate("fruit_slicer"))
    
    run = True
    SCREEN.screen.blit(current_background, (0,0))
    while run:
        clock_tick(clock, FPS)
        main_menu_button = get_main_menu_button(translate_all)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    game_menu = "main_menu"

            match game_menu:
                case "start_menu":
                    game_menu = in_start_menu(clock, FPS, main_menu_button, translate_all)

                case "main_menu":
                    game_menu = in_main_menu(clock, FPS, translate_all)

                case "score_menu":
                    game_menu = in_score_menu(clock, FPS, translate_all)
                   
                case "mode_menu":
                    game_menu, language_mode, game_mode = in_mode_menu(clock, FPS, game_mode, language_mode, translate_all)
                    translate_all.set_language(language_mode)    

                case "game_on":
                    game_menu, player = run_set_up_game(SCREEN, clock, FPS, player, translate_all)

                case "in_game":
                    game_menu, player_score = run_new_game(SCREEN, clock, FPS, game_mode, player, translate_all)

                case "menu_game_over":
                    game_menu = game_over_screen(player_score, translate_all)

                case "exit_menu":
                    exit()

        pygame.display.update() 
main()