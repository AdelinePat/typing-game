import pygame
from class_folder.Screen import Screen
from __settings__ import STYLE_FONT, BUTTON_IMAGE, ASSETS_DICT
pygame.font.init()
screen = Screen(1080, 720)

class Button:
    def __init__(self,width, height, text, identification, flip, center):
        self.text = text
        self.width = width
        self.height = height
        self.identification = identification
        self.surface = (self.width, self.height)
        self.image = pygame.transform.smoothscale(pygame.image.load(ASSETS_DICT["plank1"]).convert_alpha(), (self.surface))
        # self.center = (self.x + self.width //2, self.y + self.height // 2)
        self.center = center
        self.rect = self.image.get_rect(center = self.center)
        self.flip = flip
        self.hovered = False
        
        # self.button = pygame.Rect(self.x, self.y, 260, 40)
        self.clicked = False

    def draw(self, color):
        # pygame.draw.rect(screen.screen, 'orange', self.button, 0, 5)
        # pygame.draw.rect(screen.screen, 'beige', self.button, 5, 5)
        screen.screen.blit(self.image, self.rect)

        font_size = round(self.height // 2)
        font = pygame.font.Font(STYLE_FONT, font_size)
        dialog = font.render(self.text, True, color)

        dialog_rect = dialog.get_rect(center = self.center)
        screen.screen.blit(dialog, dialog_rect)
        

    def check_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if not self.clicked:
                self.clicked = True
                return True
        else:
            self.clicked = False
        return False
