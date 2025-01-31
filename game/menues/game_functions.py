import pygame
from class_folder.Screen import Screen
from __settings__ import FPS

def init_game_functions():
    screen = Screen(1080, 720)
    fps = FPS
    clock = pygame.time.Clock()
    player = ''
    game_mode = 'normal'
    game_menu = 'start_menu'
    pygame.init()
    return screen, fps, clock, player, game_mode, game_menu
        
def game_off():
    '''
    clear terminal, terminate pygame module and exit the program
    '''
    heavy_clear = "\033[3J\033[1;0H\033[0J"
    print(f"{heavy_clear}", end="", flush=True)
    pygame.quit()
    exit()

def clock_tick(clock,fps,frame='None'):
    '''
    the program sets the time delta on 60 times per second to update
    the screen with new informations on a regular scale
    '''
    pygame.display.update()
    clock.tick(fps)
    if frame != 'None':
        frame +=1
    return frame