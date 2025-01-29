import pygame, random
from __settings__ import FRUIT_DICT

class Fruit_slices():
    def __init__(self, x, y, size, name, screen_screen):
        self.x = x
        self.y = y
        self.size = size
        self.width = size
        self.height = size
        self.screen = screen_screen
        self.surface = (self.width, self.height)
        self.name = name
        self.image_path = FRUIT_DICT[self.name]["slice"]

        self.box_center = (self.x + self.width //2, self.y + self.height // 2)

        self.image_1 = pygame.transform.smoothscale(pygame.image.load(self.image_path).convert_alpha(), (self.surface))
        self.image_2 = pygame.transform.smoothscale(pygame.image.load(self.image_path).convert_alpha(), (self.surface))

        self.vel_y = random.randrange(20, 70)
        self.vel_x = random.randrange(-20, 20)

    def fall(self):
        if self.y < 1500:
            self.y += self.vel_y
            self.x += self.vel_x
            self.vel_y += abs(self.vel_y*0.1)


    def rotate_element(self, element):
        rotation = random.randrange(-60, 60)
        element_rotate = pygame.transform.rotate(element, rotation)
        element_rect = element_rotate.get_rect(center = self.box_center)
        return element_rotate, element_rect
    
    def draw(self):

        image_1_rotate, image_1_rect = self.rotate_element(self.image_1)
        image_2_rotate, image_2_rect = self.rotate_element(self.image_2)
        self.box_center = (self.x + self.width //2, self.y + self.height // 2)
        self.rect = self.image_1.get_rect(center = self.box_center)

        self.screen.blit(image_1_rotate, image_1_rect)
        self.screen.blit(image_2_rotate, image_2_rect)

