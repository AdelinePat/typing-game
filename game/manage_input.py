import pygame, string

def input_expression(game_mode, user_input, max_value):

    for event in pygame.event.get():
        # Handle game quit
        if event.type == pygame.QUIT:
            return game_mode, user_input, 'quit'
        # Handle keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Return to a previous menu or cancel
                return game_mode, user_input, False

            if event.key == pygame.K_RETURN and user_input != '':
                # Confirm the input when Enter is pressed
                return game_mode, user_input, True

            elif event.key == pygame.K_BACKSPACE and user_input != '':
                # Remove the last character when Backspace is pressed
                user_input = user_input[:-1]
                return game_mode, user_input, ''

            elif len(user_input) <= max_value:
                # Append valid characters to the user input
                if str(event.unicode).upper() in string.ascii_uppercase or event.unicode in (" ", "-", "'"):
                    user_input += event.unicode
                    return game_mode, user_input, ''
    # Default return if no specific action occurred
    return game_mode, user_input, ''