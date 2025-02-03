import pygame
from display.display_models.__settings__ import FROZEN_EFFECT, ICON_IMG

class Screen():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = (self.width,self.height)
        self.screen = pygame.display.set_mode(self.size)
        self.icon = self.get_icon()

    def background(self, background, caption):
        pygame.display.set_caption(caption)
        background = pygame.transform.smoothscale(background.convert_alpha(), (self.size))
        return background
        
    def frozen(self):
        frozen_effect = pygame.transform.smoothscale(FROZEN_EFFECT.convert_alpha(), (self.size))
        return frozen_effect

    def get_icon(self):
        size = (40,40)
        icon_smoothedscaled = pygame.transform.smoothscale(ICON_IMG.convert_alpha(), size)
        # icon_rotate = pygame.transform.rotozoom(icon_smoothedscaled, 25, 10)
        final_icon = pygame.display.set_icon(icon_smoothedscaled)

        return final_icon
        

