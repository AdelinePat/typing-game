import pygame
from __settings__ import BACKGROUND_IMAGE

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
