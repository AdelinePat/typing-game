import pygame
import string
from __settings__ import BACKGROUND_IMAGE
from game.menues.game_functions import clock_tick

def run_set_up_game(screen,clock,fps,game_mode,player):
    if player != '':
        user_input = player
    else: 
        user_input = ''
    current_background = screen.background(BACKGROUND_IMAGE, "Fruit Slicer")
    while True:
        screen.screen.blit(current_background, (0, 0))
        user_print = pygame.font.Font('assets/fonts/Coolvetica Rg.otf').render(user_input, True, 'black', 'white')
        user_print_rect = user_print.get_rect(center= (screen.width//2, screen.height//2))
        screen.screen.blit(user_print, user_print_rect)
        correct_input, game_mode, user_input = input_expression(game_mode, user_input, 9)
        match correct_input:
            case True:
                player = user_input
                return "in_game", game_mode, player
            case False:
                return "start_menu", game_mode, player
            case 'quit':
                return "off", game_mode, player
        clock_tick(clock,fps)

def input_expression(game_mode, user_input, max_value):
    for event in pygame.event.get():
        # Handle game quit
        if event.type == pygame.QUIT:
            return 'quit', game_mode, user_input
        # Handle keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Return to a previous menu or cancel
                return False, game_mode, user_input

            if event.key == pygame.K_RETURN and user_input != '':
                # Confirm the input when Enter is pressed
                return True, game_mode, user_input

            elif event.key == pygame.K_BACKSPACE and user_input != '':
                # Remove the last character when Backspace is pressed
                user_input = user_input[:-1]
                return '', game_mode, user_input

            elif len(user_input) <= max_value:
                # Append valid characters to the user input
                if str(event.unicode).upper() in string.ascii_uppercase or event.unicode in (" ", "-", "'"):
                    user_input += event.unicode
                    return '', game_mode, user_input
    # Default return if no specific action occurred
    return '', game_mode, user_input