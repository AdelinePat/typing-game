import pygame, random, secrets 
from class_folder.Screen import Screen
from __settings__ import MAIN_FONT

class Fruits():
    def __init__(self, x, y, size, image, rotation, devel, letter, color, screen_height, screen_screen, screen_width, name):
        self.name = name
        self.x = x
        self.y = y
        self.height = size
        self.width = size
        self.surface = (self.width, self.height)
        self.rotation = rotation
        self.color = color
        self.screen_height = screen_height
        self.screen_screen = screen_screen
        self.screen_width = screen_width
        self.box_center = (self.x + self.width//2, self.y + self.height//2)
        
        self.image =  pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (self.surface))
        
        '''TENTATIVES ADELINES
        self.vel_x = random.randrange(-4, 4)
        self.vel_y = (random.randrange(150, 275))*-1
        # self.vel_y = 50
        self.y_max = 50
        self.time_count = 0
        _____________________________________
        s = déplacement de l'objet mesuré en mettre
        u = vitesse initiale eb m/s
        t = temps
        a = acceleration
        s = u * t + (1/2) a * (t ** 2)
        self.time_count += timer
        if mode == 0:
        a = 0.01
        movement = (self.vel_y * self.time_count + 1/2 * a * timer ** 2)*0.1


        _______________________________
        if self.y > (self.screen_height + self.height + 1):
            return "dropped" # pour savoir si le fruit n'a pas pu être coupé à temps
        else:
            self.y += self.vel_y
            self.x += self.vel_x
            self.vel_y += 1 + abs(self.vel_y*0.3)
        '''

        self.letter = letter
        self.vel_x = random.randrange(-4, 4)
        self.vel_y = (random.uniform(26.75 - devel*1.75, 27.5 - devel*1.5)) * -1 # VERSION DE JOLYNE
        self.weight = self.vel_y # 59.5 - devel*5.5, 53 - devel*4

    

    def fall(self, frame, devel):
        if self.y > (self.screen_height + 2):
            return "dropped" # pour savoir si le fruit n'a pas pu être coupé à temps
        else:
            if self.x <-10 or self.x > self.screen_width-self.width+10:
                self.vel_x *= -1
            if self.vel_y < -1:
                self.y += self.vel_y
            else:
                self.y += self.vel_y*3
            self.x += self.vel_x
            if frame % 9 == 0:
                self.vel_y += abs(self.weight * (0.2 - (devel*0.01)))

    def text_render(self):
        # self.box_center = ((self.x + self.width //2) - (self.width // 50), self.y + self.height // 2)
        self.box_center = (self.x + self.width //2, self.y + self.height // 2)
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