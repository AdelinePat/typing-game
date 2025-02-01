from __settings__ import SCREEN, MAIN_FONT, BUTTON_IMAGE, BUTTON_IMAGE2, BUTTON_IMAGE3, BUTTON_IMAGE4, TEXT_COLOR, TEXT_COLOR_DARK, TEXT_COLOR_LIGHT
from display.display_models.Button_image import Button_image
from display.display_models.Button import Button

import pygame

def get_buttons():

    main_menu_button = Button_image(700, 150, 'FRUITS SLICER', "main_menu", BUTTON_IMAGE, SCREEN.screen, SCREEN.screen.get_rect().center)
    
    game_menu_button = Button_image(450, 100, "Jouer", "game_on", BUTTON_IMAGE, SCREEN.screen, ((SCREEN.width // 2), (SCREEN.height // 8)))
    mode_menu_button = Button_image(450, 100, "Mode", "mode_menu", BUTTON_IMAGE2, SCREEN.screen, ((SCREEN.width // 2), (SCREEN.height // 8) + (SCREEN.height //4)))
    score_menu_button = Button_image(450, 100, "Scores", "score_menu", BUTTON_IMAGE3, SCREEN.screen, ((SCREEN.width // 2), (SCREEN.height // 8) + (SCREEN.height //4)*2))
    exit_menu_button = Button_image(450, 100, "Quitter", "exit_menu", BUTTON_IMAGE4, SCREEN.screen, ((SCREEN.width // 2), (SCREEN.height // 8) + (SCREEN.height //4)*3))
   
    button_list = [game_menu_button, mode_menu_button, score_menu_button, exit_menu_button]

    return main_menu_button, button_list

def create_mode_menu_button():
    in_menu_button = Button_image(450, 100, "Mode", "mode_menu", BUTTON_IMAGE2, SCREEN.screen, ((SCREEN.width // 2), 70))
    difficulty_button = Button_image(300, 70, "Difficulté", "mode_menu", BUTTON_IMAGE, SCREEN.screen, ((SCREEN.width // 4), (SCREEN.height // 2 - 100)))
    language_button = Button_image(300, 70, "Langue", "mode_menu", BUTTON_IMAGE3, SCREEN.screen, ((SCREEN.width // 4)*3, (SCREEN.height // 2 - 100)))

    in_menu_button.draw(TEXT_COLOR)
    difficulty_button.draw(TEXT_COLOR)
    language_button.draw(TEXT_COLOR)

def get_difficulty_buttons():
    easy_difficulty_button = Button("Facile", "easy_mode", 28, MAIN_FONT, SCREEN.screen, ((SCREEN.width // 4), (SCREEN.height // 2 - 10)))
    normal_difficulty_button = Button("Normal", "normal_mode", 28, MAIN_FONT, SCREEN.screen, (SCREEN.width // 4, SCREEN.height // 2 + 70))
    nightmare_difficulty_button = Button("Nighmare", "nightmare_mode", 28, MAIN_FONT, SCREEN.screen, (SCREEN.width // 4, SCREEN.height // 2 + 150))
    button_mode_list = [easy_difficulty_button, normal_difficulty_button, nightmare_difficulty_button]

    return  button_mode_list

def get_language_buttons():
    french_button = Button("Français", "french_mode", 28, MAIN_FONT, SCREEN.screen, ((SCREEN.width // 4)*3, SCREEN.height // 2 - 10))
    english_button = Button("Anglais", "english_mode", 28, MAIN_FONT, SCREEN.screen, ((SCREEN.width // 4)*3, SCREEN.height // 2 + 70))
    language_list = [french_button, english_button]

    return language_list

def display_mode_menu(game_mode, language_mode):
    create_mode_menu_button()
    button_mode_list = get_difficulty_buttons()
    language_list = get_language_buttons()
        
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

def game_over_screen(player_score):
    background_screen = pygame.Surface((SCREEN.width, SCREEN.height))
    background_rect = background_screen.get_rect(center = (SCREEN.width //2, SCREEN.height // 2))
    background_screen.set_alpha(155)
    pygame.draw.rect(background_screen, (0,0,0), background_rect)
    SCREEN.screen.blit(background_screen, background_rect)

    game_over_dialog = f"Votre meilleur score est {player_score}"
    message_button = Button(game_over_dialog, "game_over_message", 42, MAIN_FONT, SCREEN.screen, (SCREEN.width//2, SCREEN.height//2 - SCREEN.height // 4.5))
    message_button.draw(TEXT_COLOR_LIGHT)

    game_over_button = Button_image(600, 150, "Perdu !", "game_over_button", BUTTON_IMAGE4, SCREEN.screen, (SCREEN.width //2, SCREEN.height // 2))
    game_over_button.draw(TEXT_COLOR_DARK)

    info_dialog_button = Button("Appuyer sur échappe ou entrer pour revenir au menu principal", "info_dialog_game_over", 30, MAIN_FONT, SCREEN.screen, (SCREEN.width//2, SCREEN.height//2 + SCREEN.height // 4.5))
    info_dialog_button.draw(TEXT_COLOR_LIGHT)

    
    

