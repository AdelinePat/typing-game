import pygame, random
from __settings__ import FRUIT_DICT

class Fruit_slices():
    def __init__(self, x, y, size, name, screen_screen, screen, fruit_half):
        self.x = x
        self.y = y
        self.size = size
        self.width = size
        self.height = size
        self.screen = screen_screen
        self.screen_width = screen.width
        self.screen_height = screen.height
        self.surface = (self.width, self.height)
        self.name = name
        self.image_path = FRUIT_DICT[self.name]["slice"]

        self.box_center = (self.x + self.width //2, self.y + self.height // 2)

        self.image = pygame.transform.smoothscale(pygame.image.load(self.image_path).convert_alpha(), (self.surface))

        self.vel_y = random.randrange(3, 8)
        if fruit_half == "half_1":
            self.vel_x = random.randrange(-8,-3)
        else: self.vel_x = random.randrange(3, 8)

    def fall(self, frame):
        if self.y > self.screen_height + 30 or -30 > self.x > self.screen_width+30:
            return 'dropped'
        else:
            self.y += self.vel_y
            self.x += self.vel_x
            if frame % 3 == 0:
                self.vel_y += abs(self.vel_y*0.2)
                if self.vel_x >= 0.5:
                    self.vel_x *= 0.8
            return None

    def rotate_element(self, element):
        rotation = random.randrange(-60, 60)
        element_rotate = pygame.transform.rotate(element, rotation)
        element_rect = element_rotate.get_rect(center = self.box_center)
        return element_rotate, element_rect
    
    def draw(self):

        image_rotate, image_rect = self.rotate_element(self.image)
        self.box_center = (self.x + self.width //2, self.y + self.height // 2)
        self.rect = self.image.get_rect(center = self.box_center)

        self.screen.blit(image_rotate, image_rect)

