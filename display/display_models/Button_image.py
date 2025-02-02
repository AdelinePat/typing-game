import pygame
from display.display_models.Button import Button
from __settings__ import STYLE_FONT

class Button_image(Button):
    def __init__(self, width, height, text, identification, image, screen, center):
        super().__init__(text, identification, height//2,  STYLE_FONT, screen, center)
        self.width = width
        self.height = height
        self.surface = (self.width, self.height)
        self.screen = screen
        self.center = center
        self.image = pygame.transform.smoothscale(image.convert_alpha(), (self.surface))
        self.image_rect = self.image.get_rect(center = self.center)
        self.hovered = False
        self.clicked = False

    def draw(self, color):
        self.screen.blit(self.image, self.image_rect)
        super().draw(color)
        return self.image_rect