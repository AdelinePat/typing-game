import pygame, random
from game.__settings__ import MAIN_FONT

class Fruits():
    def __init__(self, x, y, size, image, rotation, letter, color, screen, type):
        self.x = x
        self.y = y
        self.height = size
        self.width = size
        self.surface = (self.width, self.height)
        self.rotation = rotation
        self.color = color
        self.screen_height = screen.height
        self.screen_width = screen.width
        self.screen_screen = screen.screen
        self.type = type

        self.box_center = (self.x + self.width //2, self.y + self.height // 2)
        
        self.image =  pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (self.surface))
        self.image_rotate = pygame.transform.rotozoom(self.image, self.rotation, 1)
        self.rect_image = self.image.get_rect(center = self.box_center)
        self.letter = letter
        self.devel = 0
        self.vel_x = random.randrange(-4, 4)
        self.vel_y = (random.randrange(26, 36))*-1

    def fall(self):
        if self.y > (self.screen_height + 2):
            return "dropped" # pour savoir si le fruit n'a pas pu être coupé à temps
        else:
            if self.x <-10 or self.x > self.screen_width-self.width+10:
                self.vel_x *= -1
            self.y += self.vel_y
            self.x += self.vel_x
            if self.devel %6 == 0:
                self.vel_y += 1 + abs(self.vel_y*0.2)
            self.devel += 1

    def text_render(self):
        self.box_center = ((self.x + self.width //2) - (self.width // 50), self.y + self.height // 2)
        font_size = round(self.width // 3)
        font = pygame.font.Font(MAIN_FONT, font_size)
        
        text = font.render(self.letter, True, "white")
        text_shadow = font.render(self.letter, True, self.color)

        text_box = text.get_rect(center = self.box_center)

        text_rotate = pygame.transform.rotate(text, self.rotation)
        text_shadow_rotate = pygame.transform.rotate(text_shadow, self.rotation)

        self.screen_screen.blit(text_shadow_rotate, (text_box[0]+2, text_box[1]+2))
        self.screen_screen.blit(text_shadow_rotate, (text_box[0]-2, text_box[1]-2))
        self.screen_screen.blit(text_shadow_rotate, (text_box[0]-2, text_box[1]+2))
        self.screen_screen.blit(text_shadow_rotate, (text_box[0]+2, text_box[1]-2))

        self.screen_screen.blit(text_rotate, text_box)
        

    def draw(self):
        self.box_center = (self.x + self.width //2, self.y + self.height // 2)
        self.rect = self.image_rotate.get_rect(x=self.x, y=self.y, center=self.box_center)
        self.screen_screen.blit(self.image_rotate, self.rect)
        self.text_render()