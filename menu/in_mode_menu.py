import pygame
from __settings__ import SCREEN, TEXT_COLOR
from display.display_models.__settings__ import BACKGROUND_IMAGE_MENU
from display.display_scores import create_escape_button
from display.display_menu import display_mode_menu
from game.game_functions import clock_tick

def in_mode_menu(clock, fps, game_mode, language_mode, translator):
    
    title = translator.translate("fruit_slicer")
    location = translator.translate("main_settings")
    caption = f"{title} - {location}"
    new_background = SCREEN.background(BACKGROUND_IMAGE_MENU, caption)
    
    game_menu = "mode_menu"
    mode_menu = True

    while mode_menu:
        clock_tick(clock, fps)
        SCREEN.screen.blit(new_background, (0,0))
        
        button_mode_list, language_list = display_mode_menu(game_mode,\
                                        language_mode, translator)

        return_button = create_escape_button(translator,\
                        (SCREEN.width // 2, 7 * SCREEN.height // 8))
        return_button.draw(TEXT_COLOR)

        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    game_menu = "main_menu"
                    mode_menu = False

            if return_button.image_rect.collidepoint(mouse_position):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_menu = "main_menu"
                    mode_menu = False

            for language in language_list:
                if language.rect.collidepoint(mouse_position):
                    language.draw(TEXT_COLOR)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        language_mode = language.identification
                        translator.set_language(language_mode)
                            
            for mode_button in button_mode_list:
                if mode_button.rect.collidepoint(mouse_position):
                    mode_button.draw(TEXT_COLOR)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        game_mode = mode_button.identification

    return game_menu, language_mode, game_mode