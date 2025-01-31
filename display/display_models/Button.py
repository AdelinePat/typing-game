import pygame
class Button():
    def __init__(self, text, identification, font_size, font, screen, center):
        self.text = text
        self.identification = identification
        self.screen = screen
        self.center = center
        self.font = font
        self.font_size = font_size
    
    def draw(self, color):
        font_load = pygame.font.Font(self.font, self.font_size)
        dialog = font_load.render(self.text, True, color)

        # dialog = font_load.render(self.text, True, color)
        dialog_rect = dialog.get_rect(center = self.center)
        self.rect = dialog_rect
        self.screen.blit(dialog, dialog_rect)

        return self.rect

