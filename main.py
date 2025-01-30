from display.display_menu_assets import display_hearts, display_score_in_game
import pygame
from class_folder.Button import Button
from class_folder.Screen import Screen
from game.menues.Game_methods import Game_methods
from game.menues.Game_round import Game_round
from game.menues.Game_set_up import Game_set_up
from game.menues.Main_menu import Main_menu

from __settings__ import TEXT_COLOR

def menu_display():
    screen = Screen(1080, 720)
    background_final = screen.background()
    # screen_rect_center = screen.screen.get_rect().center
    main_menu_button = Button(700, 150, 'Menu Principal', "main_menu", 1, screen.screen.get_rect().center)
    game_menu_button = Button(450, 100, "Jouer", "game_on", 1, ((screen.width // 2), (screen.height // 8)))
    mode_menu_button = Button(450, 100, "Mode", "mode_menu", 1, ((screen.width // 2), (screen.height // 8) + (screen.height //4)))
    score_menu_button = Button(450, 100, "Score", "score_menu", 1, ((screen.width // 2), (screen.height // 8) + (screen.height //4)*2))
    exit_menu_button = Button(450, 100, "Quitter", "exit_menu", 1, ((screen.width // 2), (screen.height // 8) + (screen.height //4)*3))
    button_list = [game_menu_button, mode_menu_button, score_menu_button, exit_menu_button]
    
    run = True
    screen.screen.blit(background_final, (0,0))
   
    game_menu = "start_menu"
    clock = pygame.time.Clock()

    while run:
        # timer.tick(fps)
        timer = clock.tick(60)

        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_menu = "main_menu"

            match game_menu:
                case "start_menu":
                        screen.screen.blit(background_final, (0,0))         
                        if main_menu_button.rect.collidepoint(mouse_position):
                            main_menu_button.hovered = True
                            main_menu_button.draw("red")
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                game_menu = "main_menu"
                                # return game_menu
                        else:
                            main_menu_button.hovered = False
                            main_menu_button.draw(TEXT_COLOR)

                case "main_menu":
                    screen.screen.blit(background_final, (0,0))
                    for button in button_list:  
                        if button.rect.collidepoint(mouse_position):
                            button.hovered = True
                            button.draw("red")

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                # print("ohlalala")   
                                game_menu = button.identification
                        else:
                            button.hovered = False
                            button.draw(TEXT_COLOR)

                case "score_menu":
                    #TODO afficher les scores et les joueurs associés sur plusieurs page avec option supression
                    screen.screen.blit(background_final, (0,0))
                    score_menu_button.draw("green")

                    # exit_menu_button.draw("brown")

                case "mode_menu":
                    #TODO afficher les modes de jeu possible et les langues (si on a les temps)
                    screen.screen.blit(background_final, (0,0))
                    mode_menu_button.draw("purple")
                    # exit_menu_button.draw("blue")

                case "game_on":
                    #TODO fonction qui demande le nom d'utilisateur avant de lancer la boucle de jeu
                    new_game = Game_set_up()
                    game_menu = new_game.run()

                case "in_game":
                    new_game_start = Game_round()
                    game_menu = new_game_start.run()

                case "menu_game_over":
                    pass
                    #TODO créer le menu game over ololol



                    #TODO boucle de jeu et tout ce qui va avec


                    # game_menu_screen()
                    # screen.screen.blit(background_final, (0,0))
                    # game_menu_button.draw("black")
                    # exit_menu_button.draw("blue")
                case "exit_menu":
                    run = False
   

        # pygame.display.flip()

        pygame.display.update() 


    pygame.quit()

menu_display()