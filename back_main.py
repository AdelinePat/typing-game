import pygame
from game.Game_methods import Game_methods
from game.menues.Game_round import Game_round
from game.menues.Main_menu import Main_menu
from game.menues.Game_set_up import Game_set_up

def main():
    try:
        Game_methods()
        while True:
            match Game_methods.game_menu:
                case 'main_menu':
                    new_main_menu = Main_menu()
                    Game_methods.game_menu = new_main_menu.run()

                case 'game_set_up':
                    new_game_launch = Game_set_up()
                    Game_methods.game_menu = new_game_launch.run()

                case 'in_game':
                    new_game = Game_round()
                    Game_methods.game_menu = new_game.run()

                case 'game_off'| _:
                    Game_methods.off()
    except KeyboardInterrupt:
        Game_methods.off()
    except pygame.error:
        Game_methods.off()


main()