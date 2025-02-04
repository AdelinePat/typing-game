import pygame
from __settings__ import SCREEN, TEXT_COLOR, TEXT_COLOR_DARK
from display.display_models.__settings__ import BACKGROUND_IMAGE_MENU
from game.game_functions import clock_tick

def in_start_menu(clock, fps, main_menu_button, translator):
    """
        initiate start menu with background and button and check
        mouse input to return chosen option
    """
    title = translator.translate("fruit_slicer")

    new_background = SCREEN.background(BACKGROUND_IMAGE_MENU, title)
    SCREEN.screen.blit(new_background, (0,0))
    
    start_menu = True
    while start_menu:
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

            if main_menu_button.image_rect.collidepoint(mouse_position):
                main_menu_button.hovered = True
                main_menu_button.draw(TEXT_COLOR_DARK)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_menu = "main_menu"
                    return game_menu
            else:
                main_menu_button.hovered = False
                main_menu_button.draw(TEXT_COLOR)