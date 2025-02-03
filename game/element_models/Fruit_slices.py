import pygame, random
from __settings__ import FRUIT_DICT, SCREEN

class Fruit_slices():
    def __init__(self, x, y, vel_x, vel_y, size, name, fruit_half):
        self.x = x
        self.y = y
        self.size = size
        self.width = size
        self.height = size
        self.surface = (self.width, self.height)
        self.name = name
        self.image_path = FRUIT_DICT[self.name]["slice"]

        self.box_center = (self.x + self.width //2, self.y + self.height // 2)

        self.image = pygame.transform.smoothscale(self.image_path.convert_alpha(), (self.surface))
        self.rotation = random.randrange(-100, 100)
        self.fruit_half = fruit_half
        if -1 < abs(vel_y) < 1:
            self.vel_y = 1
        else:
            self.vel_y = abs(vel_y)
        if self.fruit_half == "half_1":
            self.vel_x = -abs(vel_x) - random.randrange(1, 5)
        elif self.fruit_half == "half_2":
            self.vel_x = abs(vel_x) + random.randrange(1, 5)

    def fall(self, frame):
        if self.y > (SCREEN.height + 2):
            return "dropped"
        else:
            if self.x <-10 or self.x > SCREEN.width-self.width+10:
                self.vel_x *= -1
            if self.vel_y < -1:
                self.y += self.vel_y
            else:
                self.y += self.vel_y*3
            self.x += self.vel_x
            if frame % 9 == 0:
                self.vel_y *= 1.5
            return None

    def rotate_element(self, element):
        self.rotation += random.randrange(10)
        
        if self.fruit_half == "half_1":
            self.rotation * -1

        element_rotate = pygame.transform.rotate(element, self.rotation)
        element_rect = element_rotate.get_rect(center = self.box_center)
        return element_rotate, element_rect
    
    def draw(self):
        image_rotate, image_rect = self.rotate_element(self.image)
        self.box_center = (self.x + self.width //2, self.y + self.height // 2)
        self.rect = self.image.get_rect(center = self.box_center)

        SCREEN.screen.blit(image_rotate, image_rect)

