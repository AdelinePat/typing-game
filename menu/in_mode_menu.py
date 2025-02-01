import pygame
from display.display_models.__settings__ import BACKGROUND_IMAGE_MENU
from display.display_menu import display_mode_menu
from __settings__ import SCREEN, TEXT_COLOR
from game.game_functions import clock_tick

def in_mode_menu(clock, fps, game_mode, language_mode):
    new_background = SCREEN.background(BACKGROUND_IMAGE_MENU, "Fruits Slicer - Modesh")
    SCREEN.screen.blit(new_background, (0,0))
    
    game_menu = "mode_menu"
    mode_menu = True

    while mode_menu:
        clock_tick(clock, fps)
        
        button_mode_list, language_list = display_mode_menu(game_mode, language_mode)
            
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    game_menu = "main_menu"
                    mode_menu = False
        
            for language in language_list:
                if language.rect.collidepoint(mouse_position):
                    language.draw(TEXT_COLOR)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        language_mode = language.identification
                            
            for mode_button in button_mode_list:
                if mode_button.rect.collidepoint(mouse_position):
                    mode_button.draw(TEXT_COLOR)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        game_mode = mode_button.identification

    return game_menu, language_mode, game_mode