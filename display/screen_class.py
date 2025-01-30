import pygame
class Screen():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = (self.width,self.height)
        self.screen = pygame.display.set_mode(self.size)

    def background(self):
        pygame.display.set_caption("Fruit Slicer")
        background = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE), (self.size))

        self.screen.blit(background, (0, 0)) # put a background picture instead of color