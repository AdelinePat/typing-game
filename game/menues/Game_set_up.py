import pygame, string
from game.Game_methods import Game_methods

class Game_set_up(Game_methods):
    def __init__(self):
        self.game_mode = Game_methods.game_mode
        self.max_value = 9

        if Game_methods.player != '':
            self.user_input = Game_methods.player
        else: 
            self.user_input = ''
        self.current_background = self.screen.background()

    def run(self):
        while True:
            self.screen.screen.blit(self.current_background, (0, 0))
            user_print = pygame.font.Font('assets/fonts/Coolvetica Rg.otf').render(self.user_input, True, 'black', 'white')
            user_print_rect = user_print.get_rect(center= (self.screen.width//2, self.screen.height//2))
            self.screen.screen.blit(user_print, user_print_rect)
            correct_input = self.input_expression()
            match correct_input:
                case True:
                    Game_methods.player = self.user_input
                    return "in_game"
                case False:
                    return "main_menu"
                case 'quit':
                    return "off"
            self.clock_tick()

    def input_expression(self):
        for event in pygame.event.get():
            # Handle game quit
            if event.type == pygame.QUIT:
                return 'quit'
            # Handle keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Return to a previous menu or cancel
                    return False

                if event.key == pygame.K_RETURN and self.user_input != '':
                    # Confirm the input when Enter is pressed
                    return True

                elif event.key == pygame.K_BACKSPACE and self.user_input != '':
                    # Remove the last character when Backspace is pressed
                    self.user_input = self.user_input[:-1]
                    return ''

                elif len(self.user_input) <= self.max_value:
                    # Append valid characters to the user input
                    if str(event.unicode).upper() in string.ascii_uppercase or event.unicode in (" ", "-", "'"):
                        self.user_input += event.unicode
                        return ''
        # Default return if no specific action occurred
        return ''
