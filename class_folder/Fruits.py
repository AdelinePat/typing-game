import pygame, random, secrets 
from class_folder.Screen import Screen
from __settings__ import MAIN_FONT

class Fruits():
    def __init__(self, x, y, size, image, rotation, letter, color, screen_height, screen_screen):
        self.x = x
        self.y = y
        self.height = size
        self.width = size
        self.surface = (self.width, self.height)
        self.rotation = rotation
        self.color = color
        self.screen_height = screen_height
        self.screen_screen = screen_screen
        self.box_center = (self.x + self.width //2, self.y + self.height // 2)
        
        self.image =  pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (self.surface))
        
        self.letter = letter
        self.vel_x = random.randrange(-4, 4)
        self.vel_y = (random.randrange(150, 275))*-1

    def fall(self):
        if self.y > (self.screen_height + self.height + 1):
            return "dropped" # pour savoir si le fruit n'a pas pu être coupé à temps
        else:
            self.y += self.vel_y
            self.x += self.vel_x
            self.vel_y += 1 + abs(self.vel_y*0.3)

    def text_render(self):
        self.box_center = ((self.x + self.width //2) - (self.width // 50), self.y + self.height // 2)
        font_size = round(self.width // 3)
        font = pygame.font.Font(MAIN_FONT, font_size)
        text = font.render(self.letter, True, "white")
        text_shadow = font.render(self.letter, True, self.color)
        text_box = text.get_rect(center = self.box_center)
        return text, text_shadow

    def rotate_element(self, element):
        element_rotate = pygame.transform.rotate(element, self.rotation)
        element_rect = element_rotate.get_rect(center = self.box_center)
        return element_rotate, element_rect

    def draw(self):
        text, text_shadow = self.text_render()

        image_rotate, rect_image = self.rotate_element(self.image)
        text_shadow_rotate, text_box_shadow_rotate = self.rotate_element(text_shadow)
        text_rotate, text_box_rotate = self.rotate_element(text)

        self.screen_screen.blit(image_rotate, rect_image)

        self.screen_screen.blit(text_shadow_rotate, (text_box_shadow_rotate[0]+2, text_box_shadow_rotate[1]+2))
        self.screen_screen.blit(text_shadow_rotate, (text_box_shadow_rotate[0]-2, text_box_shadow_rotate[1]-2))
        self.screen_screen.blit(text_shadow_rotate, (text_box_shadow_rotate[0]-2, text_box_shadow_rotate[1]+2))
        self.screen_screen.blit(text_shadow_rotate, (text_box_shadow_rotate[0]+2, text_box_shadow_rotate[1]-2))

        self.screen_screen.blit(text_rotate, text_box_rotate)