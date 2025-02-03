import pygame
from display.display_models.__settings__ import FROZEN_EFFECT

class Screen():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = (self.width,self.height)
        self.screen = pygame.display.set_mode(self.size)

    def background(self, background, caption):
        pygame.display.set_caption(caption)
        background = pygame.transform.scale(background.convert_alpha(), (self.size))
        return background
        
    def frozen(self):
        frozen_effect = pygame.transform.scale(FROZEN_EFFECT.convert_alpha(), (self.size))
        return frozen_effect
