# from display.display_game_elements import display_hearts, display_score_in_game
from display.display_menu import get_buttons, display_mode_menu
from display.display_scores import display_scores
import pygame
# from display.display_models import Button
# from display.display_models import Screen
from game.scores.Scores import Scores
from game.menues.game_functions import init_game_functions, game_off, clock_tick
from game.menues.game_round import run_new_game
from game.menues.game_set_up import run_set_up_game
from __settings__ import TEXT_COLOR
from display.display_models.__settings__ import BACKGROUND_IMAGE, BACKGROUND_IMAGE_MENU


def menu_display():
    # screen = Screen(1080, 720)
    
    screen, fps, clock, player, game_mode, game_menu, language_mode = init_game_functions()

    current_background = screen.background(BACKGROUND_IMAGE, "Fruit Slicer")
    # screen_rect_center = screen.screen.get_rect().center

    main_menu_button, main_button_list = get_buttons()
    
    
    run = True
    screen.screen.blit(current_background, (0,0))
   

    while run:
        clock_tick(clock,fps)

        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_menu = "main_menu"

            match game_menu:
                case "start_menu":
                        screen.screen.blit(current_background, (0,0))         
                        if main_menu_button.image_rect.collidepoint(mouse_position):
                            main_menu_button.hovered = True
                            main_menu_button.draw("red")
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                game_menu = "main_menu"
                                # return game_menu
                        else:
                            main_menu_button.hovered = False
                            main_menu_button.draw(TEXT_COLOR)

                case "main_menu":
                    screen.screen.blit(current_background, (0,0))
                    for main_button in main_button_list:  
                        if main_button.image_rect.collidepoint(mouse_position):
                            main_button.hovered = True
                            main_button.draw("red")

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                # print("ohlalala")   
                                game_menu = main_button.identification
                        else:
                            main_button.hovered = False
                            main_button.draw(TEXT_COLOR)

                case "score_menu":
                    #TODO afficher les scores et les joueurs associés sur plusieurs page avec option supression
                    new_background = screen.background(BACKGROUND_IMAGE_MENU, "Fruits Slicer - Scores")
                    screen.screen.blit(new_background, (0,0))
                    scores = Scores()
                    display_scores(scores.scores)
                    # score_menu_button.draw("green")


                    # exit_menu_button.draw("brown")

                case "mode_menu":
                    #TODO afficher les modes de jeu possible et les langues (si on a les temps)
                    # screen.screen.blit(current_background, (0,0))
                    # mode_menu_button.draw("purple")
                    # exit_menu_button.draw("blue")
                    new_background = screen.background(BACKGROUND_IMAGE_MENU, "Fruits Slicer - Modes")
                    screen.screen.blit(new_background, (0,0))
                    button_mode_list, language_list = display_mode_menu(game_mode, language_mode)

                    for language in language_list:
                        # for event in pygame.event.get():  
                            if language.rect.collidepoint(mouse_position):
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    language_mode = language.identification
                    for mode_button in button_mode_list: 
                            if mode_button.rect.collidepoint(mouse_position):
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    game_mode = mode_button.identification

                    # print(game_mode)
                    # print(language)

                case "game_on":
                    #TODO fonction qui demande le nom d'utilisateur avant de lancer la boucle de jeu
                    game_menu, player = run_set_up_game(screen, clock, fps, player)

                case "in_game":
                    game_menu = run_new_game(screen, clock, fps, game_mode, player)

                case "menu_game_over":
                    pass
                    #TODO créer le menu game over ololol



                    #TODO boucle de jeu et tout ce qui va avec


                    # game_menu_screen()
                    # screen.screen.blit(current_background, (0,0))
                    # game_menu_button.draw("black")
                    # exit_menu_button.draw("blue")
                case "exit_menu" | _:
                    game_off()
   

        # pygame.display.flip()

        pygame.display.update() 


menu_display()