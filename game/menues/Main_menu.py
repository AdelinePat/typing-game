import pygame
from game.Game_methods import Game_methods

class Main_menu(Game_methods):
    def __init__(self):
        pass

    def run(self):
        current_background = self.screen.background()
        self.screen.screen.blit(current_background, (0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "game_off"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return 'game_set_up'
            self.clock_tick()