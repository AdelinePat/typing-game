import pygame
from display.display_models.__settings__ import BACKGROUND_IMAGE
from __settings__ import SCREEN, TEXT_COLOR, TEXT_COLOR_DARK, FPS
from game.game_functions import clock_tick
# from display.display_menu import get_buttons

def in_main_menu(clock, fps, main_button_list):

    current_background = SCREEN.background(BACKGROUND_IMAGE, "Fruit Slicer - Menu principal")
    SCREEN.screen.blit(current_background, (0,0))
    print("blit du background dans main menu")

    while True:
        clock_tick(clock, fps)
        
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    game_menu = "main_menu"
                    return game_menu
                    # main_menu = False

            for main_button in main_button_list:  
                if main_button.image_rect.collidepoint(mouse_position):
                    main_button.hovered = True
                    main_button.draw(TEXT_COLOR_DARK)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # print("ohlalala")   
                        game_menu = main_button.identification
                        # print("game menu devrait prendre la valeur du bouton")
                        print(game_menu)
                        return game_menu
                else:
                    main_button.hovered = False
                    main_button.draw(TEXT_COLOR)
            # print("print des boutons")

        # clock_tick(clock, fps)

    # return game_menu