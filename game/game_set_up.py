import pygame
import string
from __settings__ import BUTTON_IMAGE3, SCREEN, MAIN_FONT, TEXT_COLOR_DARK,STYLE_FONT, TEXT_COLOR_LIGHT
from display.display_models.__settings__ import BACKGROUND_IMAGE, BACKGROUND_IMAGE_MENU
from display.display_models.Button import Button
from display.display_models.Button_image import Button_image
from game.game_functions import clock_tick

def run_set_up_game(screen, clock, fps, player):
    if player != '':
        user_input = player
    else: 
        user_input = ''
    current_background = SCREEN.background(BACKGROUND_IMAGE_MENU, "Fruit Slicer - Entrez votre nom d'utilisateur")
    while True:
        SCREEN.screen.blit(current_background, (0, 0))
        
        user_name_title = Button("entrez votre nom", "name_title", 42, STYLE_FONT, SCREEN.screen, (SCREEN.width//2, SCREEN.height//2 - SCREEN.height // 4.5))
        user_name_title.draw(TEXT_COLOR_LIGHT)

        info_button = Button("Appuyez sur entrer pour lancer le jeu", "info", 24, MAIN_FONT, SCREEN.screen, (SCREEN.width//2, SCREEN.height//2 + SCREEN.height // 4.5))
        info_button.draw(TEXT_COLOR_LIGHT)


        player_name_button = Button_image(600, 150, user_input, "player_input", BUTTON_IMAGE3, SCREEN.screen, (SCREEN.width//2, SCREEN.height//2))
        player_name_button.font = MAIN_FONT
        player_name_button.draw(TEXT_COLOR_DARK)

        # user_print = pygame.font.Font('assets/fonts/Coolvetica Rg.otf').render(user_input, True, 'black', 'white')

        # user_print_rect = user_print.get_rect(center= (SCREEN.width//2, SCREEN.height//2))
        # SCREEN.screen.blit(user_print, user_print_rect)
        correct_input, user_input = input_expression(user_input, 12)
        match correct_input:
            case True:
                player = user_input
                return "in_game", player
            case False:
                return "start_menu", player
            case 'quit':
                return "off", player
        clock_tick(clock,fps)

def input_expression(user_input, max_value):
    for event in pygame.event.get():
        # Handle game quit
        if event.type == pygame.QUIT:
            return 'quit', user_input
        # Handle keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Return to a previous menu or cancel
                return False, user_input

            if event.key == pygame.K_RETURN and user_input != '':
                # Confirm the input when Enter is pressed
                return True, user_input

            elif event.key == pygame.K_BACKSPACE and user_input != '':
                # Remove the last character when Backspace is pressed
                user_input = user_input[:-1]
                return '', user_input

            elif len(user_input) <= max_value:
                # Append valid characters to the user input
                if str(event.unicode).upper() in string.ascii_uppercase or event.unicode in (" ", "-", "'"):
                    user_input += event.unicode
                    return '', user_input
    # Default return if no specific action occurred
    return '', user_input