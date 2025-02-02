from __settings__ import SCREEN, MAIN_FONT, BUTTON_IMAGE, BUTTON_IMAGE2, BUTTON_IMAGE3, BUTTON_IMAGE4, TEXT_COLOR, TEXT_COLOR_DARK, TEXT_COLOR_LIGHT
from display.display_models.Button_image import Button_image
from display.display_models.Button import Button

import pygame
def get_main_menu_button(translator):   
    main_menu_text = translator.translate("main_menu")
    main_menu_button = Button_image(700, 150, main_menu_text, "main_menu", BUTTON_IMAGE, SCREEN.screen, SCREEN.screen.get_rect().center)
    return main_menu_button
     
def get_buttons(translator):
    game_menu_text = translator.translate("start_menu")
    mode_menu_text = translator.translate("main_settings")
    score_menu_text = translator.translate("score_menu")
    exit_menu_text = translator.translate("Exit_menu")

    game_menu_button = Button_image(450, 100, game_menu_text, "game_on", BUTTON_IMAGE, SCREEN.screen, ((SCREEN.width // 2), (SCREEN.height // 8)))
    mode_menu_button = Button_image(450, 100, mode_menu_text, "mode_menu", BUTTON_IMAGE2, SCREEN.screen, ((SCREEN.width // 2), (SCREEN.height // 8) + (SCREEN.height //4)))
    score_menu_button = Button_image(450, 100, score_menu_text, "score_menu", BUTTON_IMAGE3, SCREEN.screen, ((SCREEN.width // 2), (SCREEN.height // 8) + (SCREEN.height //4)*2))
    exit_menu_button = Button_image(450, 100, exit_menu_text, "exit_menu", BUTTON_IMAGE4, SCREEN.screen, ((SCREEN.width // 2), (SCREEN.height // 8) + (SCREEN.height //4)*3))
   
    button_list = [game_menu_button, mode_menu_button, score_menu_button, exit_menu_button]

    return button_list

def create_mode_menu_button(translator):
    mode = translator.translate("main_settings")
    difficulty = translator.translate("Difficulty")
    language = translator.translate("Language")

    in_menu_button = Button_image(450, 100, mode, "mode_menu", BUTTON_IMAGE2, SCREEN.screen, ((SCREEN.width // 2), 70))
    difficulty_button = Button_image(300, 70, difficulty, "mode_menu", BUTTON_IMAGE, SCREEN.screen, ((SCREEN.width // 4), (SCREEN.height // 2 - 100)))
    language_button = Button_image(300, 70, language, "mode_menu", BUTTON_IMAGE3, SCREEN.screen, ((SCREEN.width // 4)*3, (SCREEN.height // 2 - 100)))

    in_menu_button.draw(TEXT_COLOR)
    difficulty_button.draw(TEXT_COLOR)
    language_button.draw(TEXT_COLOR)

def get_difficulty_buttons(translator):
    easy = translator.translate("Easy")
    normal = translator.translate("Normal")
    difficult = translator.translate("Nightmare")

    easy_difficulty_button = Button(easy, "easy_mode", 28, MAIN_FONT, SCREEN.screen, ((SCREEN.width // 4), (SCREEN.height // 2 - 10)))
    normal_difficulty_button = Button(normal, "normal_mode", 28, MAIN_FONT, SCREEN.screen, (SCREEN.width // 4, SCREEN.height // 2 + 70))
    nightmare_difficulty_button = Button(difficult, "nightmare_mode", 28, MAIN_FONT, SCREEN.screen, (SCREEN.width // 4, SCREEN.height // 2 + 150))
    button_mode_list = [easy_difficulty_button, normal_difficulty_button, nightmare_difficulty_button]

    return  button_mode_list

def get_language_buttons(translator):
    french = translator.translate("French")
    english = translator.translate("English")

    french_button = Button(french, "fr", 28, MAIN_FONT, SCREEN.screen, ((SCREEN.width // 4)*3, SCREEN.height // 2 - 10))
    english_button = Button(english, "eng", 28, MAIN_FONT, SCREEN.screen, ((SCREEN.width // 4)*3, SCREEN.height // 2 + 70))
    language_list = [french_button, english_button]

    return language_list

def display_mode_menu(game_mode, language_mode, translator):
    create_mode_menu_button(translator)
    button_mode_list = get_difficulty_buttons(translator)
    language_list = get_language_buttons(translator)
        
    for button in button_mode_list:
        if game_mode == button.identification:
                button.draw(TEXT_COLOR)
        else:
            button.draw(TEXT_COLOR_LIGHT)

    for language in language_list:
        if language_mode == language.identification:
                language.draw(TEXT_COLOR)
        else:
            language.draw(TEXT_COLOR_LIGHT)
            
    return button_mode_list, language_list

def game_over_screen(player_score, translator):
    background_screen = pygame.Surface((SCREEN.width, SCREEN.height))
    background_rect = background_screen.get_rect(center = (SCREEN.width //2, SCREEN.height // 2))
    background_screen.set_alpha(155)
    pygame.draw.rect(background_screen, (0,0,0), background_rect)
    SCREEN.screen.blit(background_screen, background_rect)

    best_score_message = translator.translate("Game_over_message")
    game_over_button_message = translator.translate("Game_over_button")
    info_dialog = translator.translate("Info_dialog_game_over")

    game_over_dialog = f"{best_score_message} {player_score}"
    message_button = Button(game_over_dialog, "game_over_message", 42, MAIN_FONT, SCREEN.screen, (SCREEN.width//2, SCREEN.height//2 - SCREEN.height // 4.5))
    message_button.draw(TEXT_COLOR_LIGHT)

    game_over_button = Button_image(600, 150, game_over_button_message, "game_over_button", BUTTON_IMAGE4, SCREEN.screen, (SCREEN.width //2, SCREEN.height // 2))
    game_over_button.draw(TEXT_COLOR_DARK)

    info_dialog_button = Button(info_dialog, "info_dialog_game_over", 30, MAIN_FONT, SCREEN.screen, (SCREEN.width//2, SCREEN.height//2 + SCREEN.height // 4.5))
    info_dialog_button.draw(TEXT_COLOR_LIGHT)

    
    

