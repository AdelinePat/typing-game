import pygame

class Button_simple():
    # def __init__(self, text, identification, font, font_size, color):
    #     self.text = text
    #     self.identification = identification
    #     # self.font = font
    #     self.font_size = font_size
    #     # self.color = color
    #     self.hovered = False
    
    def __init__(self, text, identification, font_size, screen, center):
        self.text = text
        self.identification = identification
        # self.font = font
        self.font_size = font_size
        # self.color = color
        self.hovered = False
        self.screen = screen
        self.center = center

    def text_render(self, font, color):
        font_load = pygame.font.Font(font, self.font_size)
        dialog = font_load.render(self.text, True, color)

        # dialog = font_load.render(self.text, True, color)
        dialog_rect = dialog.get_rect(center = self.center)
        self.rect = dialog_rect
        self.screen.blit(dialog, dialog_rect)
        return self.rect


        # return dialog, dialog_rect