import pygame

def init_game_functions():
    """
        inits all major variables necessary for Pygame to run
    """
    clock = pygame.time.Clock()
    player = ''
    game_mode = 'normal_mode'
    game_menu = 'start_menu'
    language_mode = "fr"
    pygame.init()
    return clock, player, game_mode, game_menu, language_mode
        
def game_off():
    """
        clear terminal, terminate pygame module and exit the program
    """
    heavy_clear = "\033[3J\033[1;0H\033[0J"
    print(f"{heavy_clear}", end="", flush=True)
    pygame.quit()
    exit()

def clock_tick(clock,fps,frame='None'):
    """
        the program sets the time delta on 60 times per second to update
        the screen with new informations on a regular scale
    """
    pygame.display.update()
    clock.tick(fps)
    if frame != 'None':
        frame +=1
    return frame