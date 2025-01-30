import pygame
from game.class_folder.Screen import Screen
from game.__settings__ import FPS

class Game_methods:
    screen = Screen(1080, 720)
    fps = FPS
    clock = pygame.time.Clock()
    player = ''
    game_mode = 'normal'
    game_menu = 'main_menu'

    def __init__(self):
        pygame.init()
    
    def off(self):
        '''
        clear terminal, terminate pygame module and exit the program
        '''
        heavy_clear = "\033[3J\033[1;0H\033[0J"
        print(f"{heavy_clear}", end="", flush=True)
        pygame.quit()
        exit()

    def clock_tick(self,frame='None'):
        '''
        the program sets the time delta on 60 times per second to update
        the screen with new informations on a regular scale
        '''
        pygame.display.update()
        Game_methods.clock.tick(Game_methods.fps)
        if frame != 'None':
            frame +=1
        return frame