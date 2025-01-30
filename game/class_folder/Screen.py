import pygame
from game.__settings__ import BACKGROUND_IMAGE, FROZEN_EFFECT

class Screen():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = (self.width,self.height)
        self.screen = pygame.display.set_mode(self.size)

    def background(self):
        pygame.display.set_caption("Fruit Slicer")
        background = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE).convert_alpha(), (self.size))
        return background
    
    def frozen(self):
        frozen_effect = pygame.transform.scale(pygame.image.load(FROZEN_EFFECT).convert_alpha(), (self.size))
        return frozen_effect
